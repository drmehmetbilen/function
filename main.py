import os
from openai import OpenAI
import json
from function import get_folder_details, create_text_file, read_text_file, delete_file

with open("function.json",mode="r", encoding="utf-8") as file:
    function_details = json.load(file)

client = OpenAI()
def run_model_for_function(user_input):
    messageList = []
    messageList.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response =  client.chat.completions.create(
        model="gpt-4o",
        tools=function_details,
        messages=messageList
    )

    function_name = response.choices[0].message.tool_calls[0].function.name
    function_parameters = json.loads(response.choices[0].message.tool_calls[0].function.arguments)


    return function_name, function_parameters

def run_model_for_response(message_list):
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages=message_list
    )
    return response.choices[0].message.content

user_input = "deneme klasöründeki dosyaları bana liste şeklinde göster."
function_name, parameters = run_model_for_function(user_input)

if function_name == "get_folder_details":
    folder_path_from_model = parameters["folder_path"]
    function_response = get_folder_details(folder_path=folder_path_from_model)

    message_list = [
        {
            "role":"user",
            "content":user_input
        },
        {
            "role":"user",
            "content":f"Run {function_name} with parameters {folder_path_from_model}"
        },
        {
            "role":"system",
            "content":"Here are the response from the function : "+function_response + "Explain the details to the user."
        }
    ]

    last_response = run_model_for_response(message_list)
    print(last_response)

