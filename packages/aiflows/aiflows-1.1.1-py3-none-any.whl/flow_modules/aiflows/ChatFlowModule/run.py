import os

import hydra

import aiflows
from aiflows.backends.api_info import ApiInfo
from aiflows.utils.general_helpers import read_yaml_file, quick_load_api_keys

from aiflows import logging
from aiflows.flow_cache import CACHING_PARAMETERS, clear_cache

from aiflows.utils import serve_utils
from aiflows.workers import run_dispatch_worker_thread
from aiflows.messages import FlowMessage
from aiflows.interfaces import KeyInterface
from aiflows.utils.colink_utils import start_colink_server
from aiflows.workers import run_dispatch_worker_thread

CACHING_PARAMETERS.do_caching = False  # Set to True in order to disable caching
# clear_cache() # Uncomment this line to clear the cache

logging.set_verbosity_debug()

dependencies = [
    {"url": "aiflows/ChatFlowModule", "revision": os.getcwd()},
]
from aiflows import flow_verse
flow_verse.sync_dependencies(dependencies)

if __name__ == "__main__":
   
    #1. ~~~~~ Set up a colink server ~~~~
    FLOW_MODULES_PATH = "./"
    
    cl = start_colink_server()
    

    #2. ~~~~~Load flow config~~~~~~
    root_dir = "."
    cfg_path = os.path.join(root_dir, "demo.yaml")
    cfg = read_yaml_file(cfg_path)
    
    #2.1 ~~~ Set the API information ~~~
    # OpenAI backend
    api_information = [ApiInfo(backend_used="openai",
                              api_key = os.getenv("OPENAI_API_KEY"))]
    # # Azure backend
    # api_information = ApiInfo(backend_used = "azure",
    #                           api_base = os.getenv("AZURE_API_BASE"),
    #                           api_key = os.getenv("AZURE_OPENAI_KEY"),
    #                           api_version =  os.getenv("AZURE_API_VERSION") )
    
    quick_load_api_keys(cfg, api_information, key="api_infos")

    
    #3. ~~~~ Serve The Flow ~~~~
    serve_utils.serve_flow(
        cl=cl,
        flow_class_name="flow_modules.aiflows.ChatFlowModule.ChatAtomicFlow",
        flow_endpoint="ChatAtomicFlow",
    )

    #4. ~~~~~Start A Worker Thread~~~~~
    run_dispatch_worker_thread(cl)

    #5. ~~~~~Mount the flow and get its proxy~~~~~~
    proxy_flow= serve_utils.get_flow_instance(
        cl=cl,
        flow_endpoint="ChatAtomicFlow",
        user_id="local",
        config_overrides= cfg
    )
    

    #6. ~~~ Get the data ~~~
    data = {"id": 0, "question": "What is the capital of France?"}  # This can be a list of samples
    # data = {"id": 0, "question": "Who was the NBA champion in 2023?"}  # This can be a list of samples
    
 
    #option2: use the proxy_flow
    input_message = proxy_flow.package_input_message(data = data)
    
    #7. ~~~ Run inference ~~~
    future = proxy_flow.get_reply_future(input_message)
    
    #uncomment this line if you would like to get the full message back
    #reply_message = future.get_message()
    reply_data = future.get_data()
    
    # ~~~ Print the output ~~~
    print("~~~~~~Reply~~~~~~")
    print(reply_data)
    
    
    #8. ~~~~ (Optional) apply output interface on reply ~~~~
    # output_interface = KeyInterface(
    #     keys_to_rename={"api_output": "answer"},
    # )
    # print("Output: ", output_interface(reply_data))
    
    
    #9. ~~~~~Optional: Unserve Flow~~~~~~
    # serve_utils.delete_served_flow(cl, "ReverseNumberAtomicFlow_served")
    
    
