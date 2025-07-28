from sentence_transformers import SentenceTransformer, util
import fitz

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def extract_text_sections(pdf_paths):
    sections = []
    for pdf in pdf_paths:
        doc = fitz.open(pdf)
        for page_num, page in enumerate(doc):
            text = page.get_text()
            sections.append({"document": pdf, "page": page_num+1, "text": text})
    return sections

def rank_sections(persona_job, sections):
    query_embedding = model.encode(persona_job)
    ranked = []

    for section in sections:
        section_embedding = model.encode(section['text'])
        similarity = util.cos_sim(query_embedding, section_embedding).item()
        ranked.append((similarity, section))

    ranked.sort(reverse=True)
    return [section for _, section in ranked[:10]]