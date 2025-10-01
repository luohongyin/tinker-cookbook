import json
import tinker

service_client = tinker.ServiceClient()
print("Available models:")
for item in service_client.get_server_capabilities().supported_models:
    print("- " + item.model_name)

base_model = "Qwen/Qwen3-30B-A3B-Base"
training_client = service_client.create_lora_training_client(
    base_model=base_model
)

training_data = json.load(open('data/tim_long_box_processed.json'))