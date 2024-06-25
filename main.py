# libraries used:
# Streamlit: used to build the app
# langchain: used to build llm workflow
# openai: needed to use openai gpt
# wikipedia: used to connect gpt to wikipedia
# chromadb: bector storage
#Tiktoken: backend tokenzier for openai



# App framework
st.title('YOutube langchain crash coures')
prompt = st.text_input('Plug in your prompt here:')

# Prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='write me a short story about:'
)

# LLMs
llm = OpenAI(temperature = 0.7)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose = True)

# Show stuff to the screen if there is a prompt
if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)