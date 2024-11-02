 even_triangle(n):
    value = n * (n + 1) // 2
    if value % 2 == 0:
        return value
    return even_triangle(n + 1)

for i in range(1, 12):
    print(f"{i})", even_triangle(i))
  import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
v_list = []
i_list = []
e_list = []
amino_list = 'Valine','Isoleucine' ,'Glutaminc Acid'
content = fasta.read()
print('Valine'+'\t'+'Isoleucine'+'\t'+ 'Glutamic Acid'+'\n')
for line in content.split(">"):
    if re.search(r"fibroblast growth factor receptor 1 isoform", line):
        sequence = re.sub('NP.*]', '', line)
        amino = sequence[4]
        if amino in ['V']:
            v_list.append(1)
        else:
            v_list.append(0)
        if amino in ['I']:
            i_list.append(1)
        else:
            i_list.append(0)
        if amino in ['E']:
            e_list.append(1)
        else:
            e_list.append(0)

for row in v_list:
    print row
