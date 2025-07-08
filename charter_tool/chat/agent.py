from datetime import datetime
import streamlit as st

from typing import List, Optional

try:
    from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
    import torch
    HF_AVAILABLE = True
except ImportError:
    HF_AVAILABLE = False

# Global cache for the pipeline
_llm_pipeline = None

# Model selection (change as needed)
HF_MODEL_NAME = "Qwen/Qwen2-7B-Instruct"  # or "meta-llama/Llama-3-8B-Instruct"


def get_llm_pipeline(model_name=None):
    global _llm_pipeline
    if model_name is None:
        model_name = HF_MODEL_NAME
    # If the pipeline is already loaded for this model, return it
    if _llm_pipeline is not None and getattr(_llm_pipeline, 'model_name', None) == model_name:
        return _llm_pipeline
    if not HF_AVAILABLE:
        return None
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32)
        pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            device=0 if torch.cuda.is_available() else -1,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.7
        )
        pipe.model_name = model_name  # Attach for cache check
        _llm_pipeline = pipe
        return _llm_pipeline
    except Exception as e:
        print(f"[LLM] Error loading model: {e}")
        return None


# Placeholder for a real LLM agent (OpenAI, etc.)
def llm_chat_agent(prompt: str, history: Optional[List[str]] = None, model_name: Optional[str] = None, system_context: Optional[str] = None):
    """
    Use a HuggingFace LLM for chat. Falls back to the keyword-based agent if transformers is not available or model fails to load.
    """
    pipe = get_llm_pipeline(model_name)
    if pipe is not None:
        try:
            # Optionally, prepend system context and history for context
            full_prompt = prompt
            if system_context:
                full_prompt = system_context.strip() + "\n\n" + prompt
            if history:
                full_prompt = (system_context.strip() + "\n\n" if system_context else "") + "\n".join(history + [prompt])
            result = pipe(full_prompt, max_new_tokens=256)
            if isinstance(result, list) and len(result) > 0:
                return result[0]["generated_text"][len(full_prompt):].strip()
            return str(result)
        except Exception as e:
            print(f"[LLM] Generation error: {e}")
            return "[LLM Error] Could not generate a response."
    # Fallback to rules-based agent
    prompt_lower = prompt.lower()
    if any(word in prompt_lower for word in ['problem', 'solve', 'issue']):
        return "Great! Understanding the problem is crucial. Can you be more specific about the current pain points and what metrics you'd use to measure success?"
    elif any(word in prompt_lower for word in ['user', 'customer', 'people']):
        return "User analysis is key! Tell me more about their technical skills and how they currently handle this process. Are they technical or non-technical users?"
    elif any(word in prompt_lower for word in ['interface', 'ui', 'interaction']):
        return "Interface design is important! Are you thinking of a chat interface, web dashboard, API, or something else? What would work best for your users?"
    elif any(word in prompt_lower for word in ['architecture', 'system', 'components']):
        return "Let's break down the system architecture. What specialized functions do you need? Think about data processing, analysis, storage, and user interface components."
    elif any(word in prompt_lower for word in ['budget', 'cost', 'constraint']):
        return "Constraints help guide technical decisions. What's your budget, performance requirements, and any compliance needs like GDPR or security standards?"
    elif any(word in prompt_lower for word in ['timeline', 'schedule', 'deadline']):
        return "Timeline planning is crucial! What's your target go-live date? Should we plan for phases like prototype, development, testing, and deployment?"
    else:
        return "That's an interesting point! Can you elaborate on how this fits into your overall project goals? I'm here to help you structure your AI project effectively."

# Multi-agent support (future extension)
def multi_agent_chat(prompt: str, agent_type: str = "default", history=None, model_name=None, system_context=None):
    # For now, just use the default agent
    return llm_chat_agent(prompt, history, model_name, system_context)
