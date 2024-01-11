import yaml

def read_markdown_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def process_items(items):
    combined_markdown = ''
    for item in items:
        title = item['title']
        slug = item.get('slug', '')
        full_path = f"../website/content/docs/{slug}.md" if slug else ''

        # Add the title as an H1 heading
        combined_markdown += f"# {title}\n\n"

        # Add content from the corresponding Markdown file, if a slug is provided
        if slug:
            markdown_content = read_markdown_file(full_path)
            combined_markdown += f"{markdown_content}\n\n"

        # Process any nested items recursively
        if 'items' in item:
            nested_content = process_items(item['items'])
            combined_markdown += nested_content

    return combined_markdown

def main():
    with open('../website/content/docs/sidebar.yaml', 'r') as file:
        sidebar = yaml.safe_load(file)

    combined_markdown = process_items(sidebar)

    with open('markdown/neon_documentation.md', 'w') as file:
        file.write(combined_markdown)

if __name__ == "__main__":
    main()
