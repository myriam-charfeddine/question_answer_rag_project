import os

class TemplateParser:
    def __init__(self, language: str = None, default_language = "en"):
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.default_language = default_language
        self.language = None

        self.set_language(language)

    def set_language(self, language: str):
        if not language:
            self.language = self.default_language
        
        language_path = os.path.join(self.current_path, "locales", language)
        if os.path.exists(language_path):
            self.language = language

        else:
            self.language = self.default_language

    def get(self, group: str, key: str, vars: dict = {}):

        # group == file were the prompts templates are located (rag.py file in our case)
        # key == the concerned prompt (e.g: system_prompt, document_prompt, ...)
        if not group or not key:
            return None

        group_path = os.path.join(self.current_path, "locales", self.language, f"{group}.py")
        target_language = self.language

        if not os.path.exists(group_path):
            group_path = os.path.join(self.current_path, "locales", self.default_language, f"{group}.py")
            target_language = self.default_language

        if not os.path.exists(group_path):
            return None

        # import the `group` module
        module = __import__(f"stores.llm.templates.locales.{target_language}.{group}", fromlist=[group])

        if not module:
            return None
        
        # import the `key` attribute from the module
        key_attribute = getattr(module, key)

        return key_attribute.substitute(vars) # replace all the $variables in the prompt by vars
    

        

        
    
        
