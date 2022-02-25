# pip3 install openai
import os
from sys import argv
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def continue_code(code, start_output=""):
    response = openai.Completion.create(
      engine="code-davinci-001",
      prompt=code,
      temperature=0,
      max_tokens=64,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\"\"\""]
    )

    for choice in response["choices"]:
        print(f"{start_output}{choice['text']}\n###\n")

def explain_code(code, code_type="class"):
    continue_code(code + f"\n\"\"\"\nHere's what the above {code_type} is doing:\n1.", start_output="1.")

# as of Feb 24 2022, this was OpenAI's example on https://beta.openai.com/playground/p/default-explain-code?lang=python
standard_example = "class Log:\n    def __init__(self, path):\n        dirname = os.path.dirname(path)\n        os.makedirs(dirname, exist_ok=True)\n        f = open(path, \"a+\")\n\n        # Check that the file is newline-terminated\n        size = os.path.getsize(path)\n        if size > 0:\n            f.seek(size - 1)\n            end = f.read(1)\n            if end != \"\\n\":\n                f.write(\"\\n\")\n        self.f = f\n        self.path = path\n\n    def log(self, event):\n        event[\"_event_id\"] = str(uuid.uuid4())\n        json.dump(event, self.f)\n        self.f.write(\"\\n\")\n\n    def state(self):\n        state = {\"complete\": set(), \"last\": None}\n        for line in open(self.path):\n            event = json.loads(line)\n            if event[\"type\"] == \"submit\" and event[\"success\"]:\n                state[\"complete\"].add(event[\"id\"])\n                state[\"last\"] = event\n        return state\n"
# explain_code(standard_example)

runfiles = argv[1:]

for subdir in os.listdir('code-explain'):
    if os.path.isdir(os.path.join('code-explain', subdir)):
        for pypath in os.listdir(os.path.join('code-explain', subdir)):
            if '.py' in pypath and (len(runfiles) == 0 or pypath in runfiles):
                print(pypath + "\n###\n")
                with open(os.path.join('code-explain', subdir, pypath)) as codef:
                    code = codef.read()
                    if "class" in pypath:
                        code_type = "class"
                    else:
                        code_type = "function"
                    explain_code(code, code_type=code_type)


for subdir in os.listdir('code-generation'):
    if os.path.isdir(os.path.join('code-generation', subdir)):
        for pypath in os.listdir(os.path.join('code-generation', subdir)):
            if '.py' in pypath and (len(runfiles) == 0 or pypath in runfiles):
                print(pypath + "\n###\n")
                with open(os.path.join('code-generation', subdir, pypath)) as codef:
                    code = codef.read()
                    continue_code(code)
