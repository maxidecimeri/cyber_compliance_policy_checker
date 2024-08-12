import docx
import nltk

# Load NLTK resources
nltk.download('punkt')

def load_policy(file_path):
    doc = docx.Document(file_path)
    text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
    return text

def check_compliance(text):
    standards = {
        'Access Control': 'Access control measures must be implemented.',
        'Incident Response': 'An incident response plan must be in place.',
        'Data Encryption': 'Data must be encrypted at rest and in transit.',
    }
    compliance_report = {}
    for standard, requirement in standards.items():
        if requirement.lower() in text.lower():
            compliance_report[standard] = 'Compliant'
        else:
            compliance_report[standard] = 'Non-compliant'
    return compliance_report

if __name__ == "__main__":
    file_path = input("Enter the policy document file path: ")
    policy_text = load_policy(file_path)
    report = check_compliance(policy_text)
    print("Compliance Report:")
    for standard, status in report.items():
        print(f"{standard}: {status}")
