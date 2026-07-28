from dataclasses import dataclass, field


@dataclass
class LegalArticle:
    number: str
    content: str


@dataclass
class LegalChapter:
    title: str
    articles: list[LegalArticle] = field(default_factory=list)


@dataclass
class LegalLaw:
    name: str
    chapters: list[LegalChapter] = field(default_factory=list)