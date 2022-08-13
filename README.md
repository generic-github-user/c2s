# C**

(pronounced like ![](https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Prince_logo.svg/24px-Prince_logo.svg.png))

My take on a C-like programming language; main goals include pain-free macros,
comprehensive type support, object-oriented and functional style programming,
and compatibility with C and C++. This is mostly a proof of concept, so
efficiency is not a major priority; nor is completeness/usability. Wield at
your own risk.

```mermaid
graph TD
	grammar.lark --> p
	src[".c2s file"] --> p
	p[parser] --> |AST| ti
	s --> C["C/C++ code"]
	C --> gcc["C compiler"] --> binary/executable
	subgraph transpiler [T]
		ti["type inference"] --> m["macro expansion"] --> t["tree shaping"]
		t --> s[stringification]
	end
```
