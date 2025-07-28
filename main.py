import json, os
from modules.persona_intelligence import extract_text_sections, rank_sections

input_dir = '/app/input'
output_dir = '/app/output'

with open(os.path.join(input_dir, 'persona_input.json')) as f:
    persona_input = json.load(f)

persona_job = persona_input['job_to_be_done']
pdf_paths = [os.path.join(input_dir, doc) for doc in persona_input['input_documents']]

sections = extract_text_sections(pdf_paths)
ranked_sections = rank_sections(persona_job, sections)

output = {"metadata": persona_input, "extracted_sections": ranked_sections}

with open(os.path.join(output_dir, 'persona_output.json'), 'w') as f:
    json.dump(output, f, indent=2)