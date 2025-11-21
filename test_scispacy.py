import spacy

# Load small scispaCy medical model
nlp = spacy.load("en_core_sci_sm")

# Sample medical text
text = "The patient was diagnosed with hypertension and prescribed Metformin."

doc = nlp(text)

print("Detected entities:")
for ent in doc.ents:
    print(ent.text, "-", ent.label_)