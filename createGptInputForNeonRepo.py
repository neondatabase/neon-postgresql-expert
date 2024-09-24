import glob
import yaml

def read_markdown_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def process_items(items):
    combined_markdown = ''
    for item in items:
        text = read_markdown_file(item)

        # Add the title as an H1 heading
        combined_markdown += f"# Content from file {item}:\n\n"

        # Add content from the corresponding Markdown file, if a slug is provided
        combined_markdown += text + '\n\n'

    return combined_markdown

def main():
    # Create a list of files similar to the following shell command: neon % find . -name "*.md"
    file_list = glob.glob('../neon/**/*.md', recursive=True)
    file_list.sort()  # Sort the list by filename

    combined_markdown = process_items(file_list)

    with open('markdown/neon_code_readmes.md', 'w') as file:
        file.write(combined_markdown)

if __name__ == "__main__":
    main()
