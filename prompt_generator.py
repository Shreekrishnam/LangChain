from langchain_core.prompts import PromptTemplate
from langchain_core.load import dumps

template = PromptTemplate(
    template="""
Please summarize the research paper titled "{paper_input}"
in a {style_input} style and with a {length_input} length.
""",
    input_variables=["paper_input", "style_input", "length_input"]
)

template.save("template.json")