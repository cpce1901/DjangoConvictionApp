from django.shortcuts import render
from transformers import AutoModelForCausalLM, AutoTokenizer
from django.conf import settings
import os

def llama_view(request):
    # Ruta al directorio que contiene los archivos del modelo
    model_path = os.path.join(settings.BASE_DIR, "lm_models")

    # Cargar el tokenizador
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    # Cargar el modelo
    model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")

    if request.method == "POST":
        user_input = request.POST.get("user_input")
        input_ids = tokenizer.encode(user_input, return_tensors="pt")
        output = model.generate(input_ids, max_length=200, num_return_sequences=1)
        response = tokenizer.decode(output[0], skip_special_tokens=True)
    else:
        response = ""

    context = {"response": response}
    return render(request, "llama_app/llama.html", context)