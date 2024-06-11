# mistral.py
# implementer le llm mistral 7b pour repondre a la demande
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
import torch


def send_request_to_mistral(prompt, context=None):
    if context:
        prompt = context + prompt

    try:
        # Configuration pour le chargement du modèle en précision 4 bits
        bnb_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
        )

        # Chargement du tokenizer et du modèle
        tokenizer = AutoTokenizer.from_pretrained("mistral-7b")
        model = AutoModelForCausalLM.from_pretrained("mistral-7b", config=bnb_config)

        # Préparation de l'entrée pour le modèle  
        input_ids = tokenizer.encode(prompt, return_tensors='pt')

        #Génération de texte
        output = model.generate(input_ids, max_length=50, temperature=0.7)
        response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
        return response
    
    except Exception as e:
        print("Error: ", e)
        return "Je suis désolé, une erreur est survenue. Veuillez réessayer plus tard."

