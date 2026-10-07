# Sources (rule 13): every element and where it comes from

| Element | Source | Changes |
|---|---|---|
| Tokens (spacing 20 to 80, content 680 / wide 1240, fluid type, pill buttons) | Twenty Twenty-Five `theme.json` | Recolored from Shine brand: seal navy, van red, warm paper |
| Fonts: Literata + Ysabeau Office | Fonts shipped in Twenty Twenty-Five `assets/fonts` | Loaded from Google Fonts for the prototype |
| Block CSS | `@wordpress/block-library` 11.2.0 subset (`assets/css/wp-blocks.css`) | none |
| Header | TT25 `header` pattern (site logo, site title, navigation, button) | phone link added |
| Hero | Core Media & Text, `has-media-on-the-right is-image-fill-element is-stacked-on-mobile` | Gravity form in the content column |
| Forms | Gravity Forms gravity-theme markup (`gform_wrapper`, `gfield`, `gfield_required`, `gform_validation_errors`, `gf_progressbar`, multi-page) | send nothing (prototype) |
| Section labels | TT25 `is-style-text-annotation` paragraph style | |
| Services list | TT24 `cta-services-image-left` + `is-style-arrow-icon-details` Details block style | numbered |
| Lights band | Core Group on dark background (TT25 Evening variation idea) + core List | drawn SVG light string |
| About | Core Media & Text + core Gallery-style pair | |
| Steps | TT25 `services-3-col` column rhythm | guarantee seal is Shine's own SVG |
| Reviews | TT25 `testimonials-large` + core Quote `is-style-plain` | real reviews from shine-windowcleaning.com |
| Service area | Core Cover with `has-parallax`, `has-background-dim-70` | |
| FAQ | TT25 `text-faqs` with Details blocks | answers from facts.md only |
| Footer | TT25 `footer-columns` | |
| Motion | View Transitions plugin (fade), Speculative Loading (WP 6.8 core), core cover parallax, details animation | |
