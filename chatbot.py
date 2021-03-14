import aiml

kernel = aiml.Kernel()
kernel.learn("./alice/startup.xml")
kernel.respond("load aiml b")

while True:
    input_text= input("User: ")
    response=kernel.respond(input_text)
    print("Bot:"+response)