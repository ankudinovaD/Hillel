import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', encoding='utf-8') as file:
        cleaned_lines = []
        for line in file:
            cleaned_line = ''
            inside_tag = False
            i = 0
            while i < len(line):
                if line[i] == '<':
                    inside_tag = True
                elif line[i] == '>' and inside_tag:
                    inside_tag = False
                elif not inside_tag:
                    cleaned_line += line[i]
                i += 1

            cleaned_str = cleaned_line.strip()

            if cleaned_str and any(c.isalpha() for c in cleaned_str) and "=" not in cleaned_str:
                cleaned_lines.append(cleaned_str)

    with codecs.open(result_file, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(cleaned_lines))

    with codecs.open(result_file, 'r', encoding='utf-8') as result:
        print(result.read())


delete_html_tags('draft.html')
