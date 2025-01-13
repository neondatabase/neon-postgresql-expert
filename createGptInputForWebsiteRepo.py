import yaml
import os
import re


def read_markdown_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def process_items(items, base_path):
    combined_markdown = ''
    for item in items:
        title = 'noname'
        if 'title' in item:
            title = item['title']

        if 'section' in item:
            title = item['section']

        slug = item['slug'] if 'slug' in item else None       

        full_path = f"{base_path}/{slug}.md" if slug else ''

        # Add the title as an H1 heading
        combined_markdown += f"# {title}\n\n"

        # Add content from the corresponding Markdown file, if a slug is provided
        if slug:
            try:
                markdown_content = read_markdown_file(full_path)
                combined_markdown += f"{markdown_content}\n\n"
            except FileNotFoundError:
                print(f"Markdown file not found: {full_path}")
                # Skip the combined_markdown step if the file is not found
                pass

        # Process any nested items recursively
        if 'items' in item:
            nested_content = process_items(item['items'], base_path)
            combined_markdown += nested_content

    return combined_markdown

def combine_markdown_files(input_directory, output_file):
    """
    Combines all Markdown files from a directory into a single Markdown file.
    Each file is processed to extract the title from the header and include it as an H1 header.
    
    Args:
        input_directory (str): Path to the directory containing the Markdown files.
        output_file (str): Path and name of the combined Markdown file to create.
    """
    # Ensure the directory exists
    if not os.path.isdir(input_directory):
        raise ValueError(f"The directory '{input_directory}' does not exist.")

    # Get all Markdown files in alphabetical order
    markdown_files = sorted([f for f in os.listdir(input_directory) if f.endswith('.md')])

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for md_file in markdown_files:
            file_path = os.path.join(input_directory, md_file)

            with open(file_path, 'r', encoding='utf-8') as infile:
                content = infile.read()

                # Extract the title from the header
                title_match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
                title = title_match.group(1) if title_match else None

                # Add an H1 header if a title exists
                if title:
                    outfile.write(f"# {title}\n\n")
                
                # Append the full content of the markdown file
                outfile.write(content)
                outfile.write("\n\n")  # Add spacing between files

    print(f"Combined markdown saved to: {output_file}")

def main():
    with open('../website/content/docs/sidebar.yaml', 'r') as file:
        sidebar = yaml.safe_load(file)

    combined_markdown = process_items(sidebar, '../website/content/docs')

    with open('markdown/neon_documentation.md', 'w') as file:
        file.write(combined_markdown)


    # add new postgresql tutorial
    # content/postgresql/sidebar.yaml
    with open('../website/content/postgresql/sidebar.yaml', 'r') as file:
        sidebar = yaml.safe_load(file)

    combined_markdown = process_items(sidebar, '../website/content/postgresql')

    with open('markdown/postgres_tutorial.md', 'w') as file:
        file.write(combined_markdown)

    ## create content for directories not referenced in sidebar.yaml

    combine_markdown_files('../website/content/flow', 'markdown/flow.md')
    combine_markdown_files('../website/content/guides', 'markdown/guides.md')
    combine_markdown_files('../website/content/use-cases', 'markdown/use-cases.md')

if __name__ == "__main__":
    main()
