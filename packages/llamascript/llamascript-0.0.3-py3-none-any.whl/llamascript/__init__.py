import ollama

class llama:
    def __init__(self):
        self.model = None
        self.data = None
        self.system = None
        self.ignore = False
    
    def USE(self, line):
        if line.split(' ')[0] == 'USE':
            self.model = line.split(' ')[1]
        else:
            raise ValueError('Invalid model')
    
    def PROMPT(self, line):
        if line.split(' ')[0] == 'PROMPT':
            self.data = line.split(' ')[1]
        else:
            raise ValueError('Invalid data')
    
    def SYSTEM(self, line):
        if line.split(' ')[0] == 'SYSTEM':
            prompt = line.split(' ')[1]
            self.system = [{'role': 'system', 'content': prompt}]
        else:
            raise ValueError('Invalid system prompt.')
    
    def CHAT(self):
        try:
            print(ollama.chat(model=self.model, messages=[{self.system} if self.system else {'role': 'system', 'content': ''}, {'role': 'user', 'content': self.data}])['message']['content'])
        except:
            try:
                print('Model not loaded. Trying to load model...')
                ollama.pull(self.model)
                self.CHAT()
            except:
                raise ValueError('Model does not exist or could not be loaded. Please try again.')
    
    def read(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                command = line.split(' ')[0]
                if command == 'IGNORE':
                    self.ignore = True
                elif command == 'USE':
                    self.USE(line)
                elif command == 'PROMPT':
                    self.PROMPT(line)
                elif command == 'CHAT':
                    if not self.ignore:
                        print('=================\nThanks for using llama, a no-code AI chatbot. Please ensure Ollama (https://ollama.com) is running. To get started, type "USE" followed by the model you want to use. Then, type "PROMPT" followed by the prompt you want to use. Finally, type "CHAT" to chat with the AI. To run a script, type "llamascript" to run your script. To ignore this message, add "IGNORE" to the beginning of your llama file.\n=================')
                        self.ignore = True
                    self.CHAT()
                else:
                    raise ValueError('Invalid command')
                

def run():
    try:
        l = llama()
        l.read('llama')
    except KeyboardInterrupt:
        pass
