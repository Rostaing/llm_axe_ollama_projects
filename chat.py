from llm_axe import OnlineAgent, OllamaChat, PdfReader
llm = OllamaChat(model="llama3:instruct")

pdfReader = PdfReader(llm)
resp = pdfReader.ask("De quoi parle ce document et a qui appartient cela ?", ["doc.pdf"])
# onlineAgent = OnlineAgent(llm)

# resp = onlineAgent.search(resp + "\n What is his nationality about?")
print(resp)

# from llm_axe import OnlineAgent, OllamaChat 

# llm = OllamaChat(model= "llama3:instruct" ) 
# online_agent = OnlineAgent(llm) 

# prompt = "Parlez-moi un peu de ce site Web :https://riviera-realisation.com/??"
# resp = online_agent.search(prompt) 
# print (resp)