
with open('test.text', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test.text', 'w') as writer:
        for line in reversed(content):
            writer.write(line)