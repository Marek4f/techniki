## Techniki Internetowe, 14/15

> *Uważaj na człowieka, którego nie interesują szczegóły.*
>
> — William Feather

Terminy rozliczenia się z projektów:

* ***zaliczenie***: **ISODate("2015-03-24T12:00:00.000Z")**<br>
  nierozliczenie się z projektu w terminie powoduje obniżenie oceny
* ***egzamin***: **ISODate("2015-05-12T12:00:00.000Z")**<br>
  nierozliczenie się z projektu w terminie oznacza ocenę ndst
  z egzaminu; na egzamin poprawkowy zostaną wyznaczone nowe projekty

Projekty tworzymy w repozytoriach Git na *GitHub* lub *Bitbucket*.
Projekt na egzamin umieszczamy w repozytorium prywatnym.
W repozytoriach nie powinno być śmieci, np. plików backup edytora.


### Zaliczenie

1\. Zapoznajemy się z notacjami:

* [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) –
  Github-flavored
* [reStructuredText Primer](http://sphinx-doc.org/rest.html)
* [AsciiDoc](http://www.methods.co.nz/asciidoc/); zob. też
  [Pro Git Book, ed. 2](https://github.com/progit/progit2)

Korzystając z jednej z tych notacji przygotować:

* tabelkę porównującą te notacje; przepisać tę tabelkę w *czystym* HTML5
* przygotować tabelkę z programem MŚ w Falun 2015 lub programu TV z jednego dnia

W których z tych notacji można wpisywać wzory w notacji LaTeX? (zob. na przykład
[Math in reStructuredText with LaTeX](http://stackoverflow.com/questions/3610551/math-in-restructuredtext-with-latex)).

2\. [GitHub Pages](https://pages.github.com).
Przygotować responsywne *user* lub *project site* korzystające
z jednego z frameworków:

* [Foundation](http://foundation.zurb.com)
* [Bootstrap](http://getbootstrap.com)

Na stronach wstawić mapkę korzystającą [Leaflet](http://leafletjs.com/)
oraz użyć kilku *web components* z biblioteki [Polymer](https://www.polymer-project.org).

<!--
Dane należy wpisać według formatu (wszystko w jednym wierszu):

    1. [Nazwisko Imię](link do repozytorium z kodem).
       [Nazwa aplikacji korzystającej z Leaflet](link do działającej aplikacji),
       [Tytuł prezentacji](link do działających slajdów).
-->


### Egzamin

1\. Przygotować prostą aplikację WWW korzystając z frameworka [Meteor](https://www.meteor.com/).
Do kodu *JavaScript* dopisać testy (co najmniej kilkanaście).
Testy podłączyć do platformy [Travis](https://travis-ci.com/plans) (wybrać FREE plan).

2\. Przygotować pokaz slajdów w [Reveal.js](http://lab.hakim.se/reveal-js/)
szczegółowo opisujący jak wdrożyć [przykładową aplikację Meteor](https://www.meteor.com/install)
na zewnętrznym serwerze
[Digital Ocean](http://devo.ps/blog/deploy-your-meteor-apps-on-digital-ocean-in-5-minutes/)
lub [Heroku](http://ondrej-kvasnovsky.blogspot.com/2013/05/how-to-deploy-meteor-on-heroku-with.html).

Po instalacji frameworka [Meteor](https://www.meteor.com/install)
listę przykładowych aplikacji wypisze to polecenie:
```console
$ meteor create --list
```

<!--
Dane należy wpisać według formatu (wszystko w jednym wierszu):

    1. [Nazwisko Imię](link do repozytorium z kodem).
    [Nazwa aplikacji](link do wdrożonej i działającej aplikacji)

U góry strony *README.md* w repozytorium z kodem dodać ikonkę Travisa [build|passing],
tak jak to zrobiono na stronie [RSpec Intro](https://github.com/wbzyl/ruby-intro).
-->


### 2015 → ∞

[JavaScript in 2015](http://glenmaddern.com/articles/javascript-in-2015)
([YouTube](https://www.youtube.com/watch?v=iukBMY4apvI)):

- Nicholas C. Zakas.
  [Understanding ECMAScript 6](https://leanpub.com/understandinges6/read/)
- [ES.next showcase](https://github.com/sindresorhus/esnext-showcase)
  - [JavaScript Promises ... In Wicked Detail](http://mattgreer.org/articles/promises-in-wicked-detail/)
- [Web Components](http://w3c.github.io/webcomponents/explainer/):
  * Addy Osmani.
  [The Web’s Declarative, Composable Future](http://addyosmani.com/blog/the-webs-declarative-composable-future/)

CSS in 2015:

- [Less](http://lesscss.org)
- [Sass](http://sass-lang.com)

Reszta:

- [Pro Git Book](http://git-scm.com/book/en/v2)
- [Docker](http://www.docker.com/) –  Build, Ship and Run Any App, Anywhere
- [Meteor](https://www.meteor.com/):
  [Discover Meteor](http://book.discovermeteor.com/)
  ([polskie tłumaczenie](http://pl.discovermeteor.com/))


### Różne rzeczy

- [GitHub Flavored Markdown](http://guides.github.com/overviews/mastering-markdown/) +
  [Mastering Markdown](http://guides.github.com/overviews/mastering-markdown/)
- [Mapping geoJSON files on GitHub](https://help.github.com/articles/mapping-geojson-files-on-github)
