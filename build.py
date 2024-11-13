import json
import os

def load_publication(publication_path):
    with open(publication_path, 'r') as project_file:
        project = json.load(project_file)

    return project


def build_publication_link(publication):
    output = ""
    output += f"\t\t\t<li class=\"project-item  active\" data-filter-item data-category=\"{publication['category'].lower()}\">\n"
    output += f"\t\t\t\t<a href=\"#\" class=\"navbar-link\" data-nav-link=\"{publication['slug']}\">\n"
    output += f"\t\t\t\t\t<figure class=\"project-img\">\n"
    output += f"\t\t\t\t\t\t<div class=\"project-item-icon-box\">\n"
    output += f"\t\t\t\t\t\t\t<ion-icon name=\"eye-outline\"></ion-icon>\n"
    output += f"\t\t\t\t\t\t</div>\n"
    output += "\n"
    output += f"\t\t\t\t\t\t<img src=\"./assets/images/{publication['image']}\" alt=\"{publication['alt-tag']}\" loading=\"lazy\">\n"
    output += "\t\t\t\t\t</figure>\n"
    output += "\n"
    output += f"\t\t\t\t\t<h3 class=\"project-title\">{publication['title']}</h3>\n"
    output += "\n"
    output += f"\t\t\t\t\t<p class=\"project-category\">{publication['category']}</p>\n"
    output += "\n"
    output += "\t\t\t\t</a>\n"
    output += "\t\t\t</li>\n"
    return output

def build_publication_page(publication):
    output = ""
    output += f"\t\t\t<article class=\"blog\" data-page=\"{publication['slug']}\">\n"
    output += "\t\t\t\t<header>\n"
    output += f"\t\t\t\t\t<h2 class=\"h2 article-title\">{split_title(publication['title'])}</h2>\n"
    output += "\t\t\t\t</header>\n"
    output += "\t\t<ul class=\"paper-list\">\n"
    output += f"\t\t\t\t<li class=\"paper-item\">\n"
    output += f"\t\t\t\t\t<a href=\"{publication['paper']}\">\n"
    output += f"\t\t\t\t\t\t<h4 class=\"h4 paper-title\">Paper</h4>\n"
    output += f"\t\t\t\t\t</a>\n"
    output += f"\t\t\t\t</li>\n"
    if 'code' in publication:
        output += f"\t\t\t\t<li class=\"paper-item\">\n"
        output += f"\t\t\t\t\t<a href=\"{publication['code']}\">\n"
        output += f"\t\t\t\t\t\t<h4 class=\"h4 paper-title\">Code</h4>\n"
        output += f"\t\t\t\t\t</a>\n"
        output += f"\t\t\t\t</li>\n"
    if 'dataset' in publication:
        output += f"\t\t\t\t<li class=\"paper-item\">\n"
        output += f"\t\t\t\t\t<a href=\"{publication['dataset']}\">\n"
        output += f"\t\t\t\t\t\t<h4 class=\"h4 paper-title\">Dataset</h4>\n"
        output += f"\t\t\t\t\t</a>\n"
        output += f"\t\t\t\t</li>\n"
    output += "\t\t</ul>\n"   

    output += build_page_content(os.path.join('publications', publication['markdown']))
    output += "\t\t\t</article>\n"
    return output

def split_title(title, max_length=30):
    if len(title) <= max_length:
        return title
    else:
        words = title.split()
        new_title = "<p>"
        subtitle = ""
        for i, word in enumerate(words):
            if len(subtitle) + len(word) > max_length:
                new_title = subtitle + "</p><p>" + " ".join(words[i:]) + "</p>"
                return new_title
            subtitle += word + " "

def build_page_content(markdown):
        
    output = ""
    output += f"\t\t<section class=\"about-text\">\n"
    with open(markdown, 'r') as infile:
        for line in infile:
            output += f"\t\t\t<p>\n"
            output += f"\t\t\t\t{line}"
            output += f"\t\t\t</p>\n"
    output += "\t\t</section>\n"
    return output


PUBLICATIONS = [
    "paradocs.json",
    "ctxpro.json",
    "language-tokens.json",
    "importance-of-segmentation.json",
    "ersatz.json",
    "jhubc.json"]



if __name__ == "__main__":

    index_file = open('template.html').read()

    publications_links = []
    publication_pages = []
    # for _, _, publications in os.walk('publications'):
    for publication in PUBLICATIONS:
        if publication.endswith(".json"):
            pub = load_publication(f"publications/{publication}")
            publications_links.append(build_publication_link(pub))
            publication_pages.append(build_publication_page(pub))
    index_file = index_file.replace('```INSERT_PUBLICATION_LINKS_HERE```', "\n".join(publications_links))
    index_file = index_file.replace('```INSERT_PUBLICATION_PAGES_HERE```', "\n".join(publication_pages))

    print(index_file)