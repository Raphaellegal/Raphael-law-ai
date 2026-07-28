import re

from app.models.legal_structure import (
    LegalLaw,
    LegalChapter,
    LegalArticle
)


class LegalParser:
    """
    Parses legal documents into a legal hierarchy.
    """

    def parse(self, text: str, law_name: str):

        law = LegalLaw(
            name=law_name
        )

        current_chapter = None
        current_article = None
        article_content = []

        for raw_line in text.splitlines():

            line = raw_line.strip()

            if not line:
                continue


            if re.match(
                r"^(SECTION|CHAPTER|CHAPITRE|TITLE|TITRE)",
                line,
                re.IGNORECASE
            ):

                if current_article and current_chapter:
                    current_article.content = "\n".join(article_content)
                    current_chapter.articles.append(current_article)


                article_content = []

                current_chapter = LegalChapter(
                    title=line
                )

                law.chapters.append(
                    current_chapter
                )

                current_article = None

                continue


            if re.match(r"^ARTICLE", line, re.IGNORECASE):

                print("ARTICLE FOUND:", line)

                if current_article and current_chapter:
                    current_article.content = "\n".join(article_content)
                    current_chapter.articles.append(current_article)


                article_content = []

                current_article = LegalArticle(
                    number=line,
                    content=""
                )

                continue


            article_content.append(line)


        if current_article and current_chapter:
            current_article.content = "\n".join(article_content)
            current_chapter.articles.append(
                current_article
            )

        if not law.chapters:

            chapter = LegalChapter(
                title="GENERAL"
            )

            article = LegalArticle(
                number="UNKNOWN",
                content=text
            )

            chapter.articles.append(article)

            law.chapters.append(chapter)

        return law