# pip3 install transformers
import os
from sys import argv
from time import sleep

from transformers import AutoModelForCausalLM, AutoTokenizer

#from simpletransformers.language_generation import LanguageGenerationModel

tokenizer = None
model = None

def continue_code(subdir, pypath, model_name, start_output=""):
    with open(os.path.join('code-generation', subdir, pypath)) as codef:
        code = codef.read()
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        content = tokenizer.encode(code, return_tensors='pt')
        print([model_name, subdir, pypath])

        typ_output = model.generate(
            content,
            max_length=50,
            # num_beams=1,  #?
            early_stopping=True,
            do_sample=False, # True,
            # typical_p=0.85, #?
            repetition_penalty=4.0, #?
            # log_decoder=True,
        )

        txt = tokenizer.decode(typ_output[0], skip_special_tokens=True)
        open('./log-outputs/' + subdir + '_' + pypath.replace('.py', '') + '_'
            + model_name.replace('/', '_') + '_result.py', 'w').write(f"{start_output}{txt}\n")

# as of Feb 24 2022, this was OpenAI's example on https://beta.openai.com/playground/p/default-explain-code?lang=python
standard_example = "class Log:\n    def __init__(self, path):\n        dirname = os.path.dirname(path)\n        os.makedirs(dirname, exist_ok=True)\n        f = open(path, \"a+\")\n\n        # Check that the file is newline-terminated\n        size = os.path.getsize(path)\n        if size > 0:\n            f.seek(size - 1)\n            end = f.read(1)\n            if end != \"\\n\":\n                f.write(\"\\n\")\n        self.f = f\n        self.path = path\n\n    def log(self, event):\n        event[\"_event_id\"] = str(uuid.uuid4())\n        json.dump(event, self.f)\n        self.f.write(\"\\n\")\n\n    def state(self):\n        state = {\"complete\": set(), \"last\": None}\n        for line in open(self.path):\n            event = json.loads(line)\n            if event[\"type\"] == \"submit\" and event[\"success\"]:\n                state[\"complete\"].add(event[\"id\"])\n                state[\"last\"] = event\n        return state\n"
# explain_code(standard_example)

runfiles = argv[1:]

models = [
    # 'gpt2',
    # 'codeparrot/codeparrot-small',
    'codeparrot/codeparrot',
    'EleutherAI/gpt-j-6B',
]

for subdir in os.listdir('code-generation'):
    if os.path.isdir(os.path.join('code-generation', subdir)):
        for model_name in models:
            for pypath in os.listdir(os.path.join('code-generation', subdir)):
                if '.py' in pypath and (len(runfiles) == 0 or pypath in runfiles):
                    continue_code(subdir, pypath, model_name)
            if model is not None:
                del model
            if tokenizer is not None:
                del tokenizer
