%global extension   pop-shell
%global uuid        %{extension}@system76.com
%global commit      6c2de1d379ccd9d6a854e107192e08637efdaf18
%global shortcommit %{sub %{commit} 1 7}

Name:           gnome-shell-extension-%{extension}
Version:        1.2.0^32.%{shortcommit}
Release:        %autorelease
Epoch:          1
Summary:        GNOME Shell extension for advanced tiling window management
License:        GPL-3.0-only
URL:            https://github.com/adil192/pop-shell
BuildArch:      noarch

%undefine       _disable_source_fetch
Source0:        %{url}/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz

Source1:        50_org.gnome.desktop.wm.keybindings.%{extension}.gschema.override
Source2:        50_org.gnome.mutter.%{extension}.gschema.override
Source3:        50_org.gnome.mutter.wayland.%{extension}.gschema.override
Source4:        50_org.gnome.settings-daemon.plugins.media-keys.%{extension}.gschema.override
Source5:        50_org.gnome.shell.%{extension}.gschema.override
# downstream-only
Patch:          0001-Remove-schema-handling-from-transpile.sh.patch

# START NPM SOURCES
Source100:      https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.10.1.tgz
%define         SHA512SUM100 cuadcxVFE8sDK6iWJbs8Sn0av2Nrh2QSGQhVlBW9AaAHqHwjWsZHT8LJ4hFGPh7ASBV2deFdM7H/DPjulmh8rg==
Source101:      https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-3.4.3.tgz
%define         SHA512SUM101 wpc+LXeiyiisxPlEkUzU6svyS1frIO3Mgxj1fdy7Pm8Ygzguax2N3Fa/D/ag1WqbOprdI+uY6wMUl8/a2G+iag==
Source102:      https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz
%define         SHA512SUM102 EriSTlt5OC9/7SXkRSCAhfSxxoSUgBm33OH+IkwbdpgoqsSsUg7y3uh+IICI/Qg4BBWr3U2i39RpmycbxMq4ew==
Source103:      https://registry.npmjs.org/@eslint/config-array/-/config-array-0.23.5.tgz
%define         SHA512SUM103 Y3kKLvC1dvTOT+oGlqNQ1XLqK6D1HU2YXPc52NmAlJZbMMWDzGYXMiPRJ8TYD39muD/OTjlZmNJ4ib7dvSrMBA==
Source104:      https://registry.npmjs.org/@eslint/config-helpers/-/config-helpers-0.7.0.tgz
%define         SHA512SUM104 DObd/KKUsU+FaFv4PLxSRenpXfQWmPXXP3pPZ6/K1PCrMu2vQpMDMuQe/BqYeoLcz8ro0bVDF1RxOJgfVEdhUw==
Source105:      https://registry.npmjs.org/@eslint/core/-/core-1.2.1.tgz
%define         SHA512SUM105 MwcE1P+AZ4C6DWlpin/OmOA54mmIZ/+xZuJiQd4SyB29oAJjN30UW9wkKNptW2ctp4cEsvhlLY/CsQ1uoHDloQ==
Source106:      https://registry.npmjs.org/@eslint/js/-/js-10.0.1.tgz
%define         SHA512SUM106 zeR9k5pd4gxjZ0abRoIaxdc7I3nDktoXZk2qOv9gCNWx3mVwEn32VRhyLaRsDiJjTs0xq/T8mfPtyuXu7GWBcA==
Source107:      https://registry.npmjs.org/@eslint/object-schema/-/object-schema-3.0.5.tgz
%define         SHA512SUM107 vqTaUEgxzm+YDSdElad6PiRoX4t8VGDjCtt05zn4nU810UIx/uNEV7/lZJ6KwFThKZOzOxzXy48da+No7HZaMw==
Source108:      https://registry.npmjs.org/@eslint/plugin-kit/-/plugin-kit-0.7.2.tgz
%define         SHA512SUM108 +CNAzxglkrpNf/kKywqQfk74QjtceuOE7Qm+AF8miRvPF/wmmK5+OJOgVh3AVTT3RP2mH3+FOaxlE5v72owk0A==
Source109:      https://registry.npmjs.org/@girs/accountsservice-1.0/-/accountsservice-1.0-4.1.0.tgz
%define         SHA512SUM109 Kp8TXbun34nQJ6h0EOqmAJ8P8sd3huzJMPtdw2FOpTPzViFcUPC95fICi231Ur0FhfhH62lXZnHthifUKb01HQ==
Source110:      https://registry.npmjs.org/@girs/adw-1/-/adw-1-4.1.0.tgz
%define         SHA512SUM110 Xv4doRXq7o9K+plUlrjl7e6ba04jtc7JS6U8JEMGZuNOL0BXsZa2lNbnLKKjUQnwzbh80EDECgyhiBkbhq7Heg==
Source111:      https://registry.npmjs.org/@girs/atk-1.0/-/atk-1.0-4.1.0.tgz
%define         SHA512SUM111 GBf3Ehc56boCbDx9lOt4hMWaETgxsUZ33Bfk022BVHhvWwXd5iWFt9wQHTiFkgJcAJjmPavhkouniAbuuBwH4Q==
Source112:      https://registry.npmjs.org/@girs/cairo-1.0/-/cairo-1.0-4.1.0.tgz
%define         SHA512SUM112 iCdRmpCPpQn+skaJfLsDUvSSidKgQLAsFeah5Ac5I5dRmpdwCvDTsox6wreZssfhERWcUAldtWj7wXmSzPBLKg==
Source113:      https://registry.npmjs.org/@girs/clutter-18/-/clutter-18-4.1.0.tgz
%define         SHA512SUM113 1peMQVW/Uu22YoEG8Msx8lRQgOXy1Efuw2al03v6Lc0yWdAXdL8aWZ4d8p6YKAH6WTBmiMthWG60+bZqKur0Cw==
Source114:      https://registry.npmjs.org/@girs/cogl-18/-/cogl-18-4.1.0.tgz
%define         SHA512SUM114 eykux7piDFKlAoNpuEdzi7FjrD3TbSNlGCUHgKkkV8NEgU0WQr+SH15yCVMJDlqR4cxH8byESOaiXginEBIgEg==
Source115:      https://registry.npmjs.org/@girs/freetype2-2.0/-/freetype2-2.0-4.1.0.tgz
%define         SHA512SUM115 /+fMzCY84TrKi5wcT/EVQulM9xPhCAA5cTaZclzufA01MvasA8vrPu5zEF8qhfYbm77ro94A8P6kWpcOf1LxEQ==
Source116:      https://registry.npmjs.org/@girs/gck-2/-/gck-2-4.1.0.tgz
%define         SHA512SUM116 jrFH1iWhkGxFG2jCS+NYzWBM6jcaNYNysA3r9AT+EWmY7kVkMeGi9ec+LSqIqjC0qU/MaHaLIZ6HU6o34zZU3Q==
Source117:      https://registry.npmjs.org/@girs/gcr-4/-/gcr-4-4.1.0.tgz
%define         SHA512SUM117 gpwN7hDZDg7ZFvVKhQcRIm5BhmcprFigtn6NR5Kohsquc6YGiq70v9Xo19gmWRQMFMo3nB+mZAAjzvTbpXhCww==
Source118:      https://registry.npmjs.org/@girs/gdesktopenums-3.0/-/gdesktopenums-3.0-4.1.0.tgz
%define         SHA512SUM118 itkzeTHIezAVpuQgqDPKPPt00KOUZRPPdQBU4Ac/4/nKZTcmKwPFfLgQjgkcX1V4UQYknvGFoEY2E8X2tJagiQ==
Source119:      https://registry.npmjs.org/@girs/gdk-3.0/-/gdk-3.0-4.1.0.tgz
%define         SHA512SUM119 CFDjHJ7frLtqZXLLFnqeCGfPOyPrzlX3g8sAAhWJnjrqPShEXmFuXXOOOyZfQXcxynHTIx0rPSOiujH9ZNSTHw==
Source120:      https://registry.npmjs.org/@girs/gdk-4.0/-/gdk-4.0-4.1.0.tgz
%define         SHA512SUM120 Wf7ZaDS2e+DUJwEBVn/DQux42b2KQYNhWeaheK7nx5Ia6Y/w3Xpm/yqqYJh+KnZ+y8IgypjpscjL4qBkr944rw==
Source121:      https://registry.npmjs.org/@girs/gdkpixbuf-2.0/-/gdkpixbuf-2.0-4.1.0.tgz
%define         SHA512SUM121 i89aPIgZPSD1/UNH5PlsT7660HtqfPu8eU5TeSedUV7H5kCWXRO11SqbRpGJoa3ScMu8UU0LOkgFB1f1x0QefA==
Source122:      https://registry.npmjs.org/@girs/gdm-1.0/-/gdm-1.0-4.1.0.tgz
%define         SHA512SUM122 JwIbQx1ABn0FSahUCXFyTrPkF7W38z6wyx2ydW+5ge5j2YKJTmadFd+/vK4BKyJgwkH9IjseLeWXzUrhQurBKQ==
Source123:      https://registry.npmjs.org/@girs/gio-2.0/-/gio-2.0-4.1.0.tgz
%define         SHA512SUM123 irRUpGEOHknlk4TNoOlAaBCg/jCGZKZv8Ulr23mmqf+MTI6ygDcbJY6bdHAf5dZfbgkOXjhXRl753j8F850W9Q==
Source124:      https://registry.npmjs.org/@girs/giounix-2.0/-/giounix-2.0-4.1.0.tgz
%define         SHA512SUM124 e3JbHrw+MDbY4NzgMAIh7OUkA7bRfe8AuivklDPNF4b42q+ROyY2A1FZ+wYWGDYuRcjj8vokgDYIJ9hFy1wbAQ==
Source125:      https://registry.npmjs.org/@girs/gjs/-/gjs-4.1.0.tgz
%define         SHA512SUM125 fF6beHhI/DW/4WF2JVDRVpjnWuae93euyr4NXOOTNXwaatDxbMB21jte+b0+Qc7eUEqjIUhV10Hq6ztl4hKWQg==
Source126:      https://registry.npmjs.org/@girs/gl-1.0/-/gl-1.0-4.1.0.tgz
%define         SHA512SUM126 DO2ibBPLGJe9IRWjQQ1zR7bVjk6yBWsvnN1W1fCweNItavJ2+fwTkyo8uHUnYtn5X2FIlx+drkO8VggFnbwdVA==
Source127:      https://registry.npmjs.org/@girs/glib-2.0/-/glib-2.0-4.1.0.tgz
%define         SHA512SUM127 1OeIRobL8UEPP5HXD+lwEgM3643aof+mJ6GJD6TMtzuI9ZbuVyS9MJjQopHW+YrRSLAZwfSQXm2WipA3p3EZmg==
Source128:      https://registry.npmjs.org/@girs/gmodule-2.0/-/gmodule-2.0-4.1.0.tgz
%define         SHA512SUM128 yOFTdnvD61ohMDk12T2Rhcve6vP4/vZpwb/0iQYLu4ZOTD6cazMEdpM+ncZSj8beffbRqTfd7H81HNAriVVm5Q==
Source129:      https://registry.npmjs.org/@girs/gnome-shell/-/gnome-shell-50.0.4.tgz
%define         SHA512SUM129 69phtdJHMPUBxVRDqfE4JWSZeauTIl0zFuILMIkJbqyHOb1U9sxN7yN59x+pJWGxVTktFz/Y9uXKjDzOcHlYFA==
Source130:      https://registry.npmjs.org/@girs/gnomebg-4.0/-/gnomebg-4.0-4.1.0.tgz
%define         SHA512SUM130 9uha/ow4xAEqTiUkd0ew3vRlYTz3YHSG3HMQiGcVYdE/pWHFHjXQ5pToOIyQoDLL+HhoFy7XCUCCBxkgTuSk7w==
Source131:      https://registry.npmjs.org/@girs/gnomebluetooth-3.0/-/gnomebluetooth-3.0-4.1.0.tgz
%define         SHA512SUM131 V0Lo4JE0jotRbXZume/ZpoxUDyX8u1Iw8TD7i26iaMcsTQkNaEJdoNZfhL2WVW1rTU4pwkHD8IGJ2jZLTGInhA==
Source132:      https://registry.npmjs.org/@girs/gnomedesktop-4.0/-/gnomedesktop-4.0-4.1.0.tgz
%define         SHA512SUM132 Rh1kcycDgjI29sjuP+72SODLEqYKxVAZ+FV5DUBmDOVjfNLTlIPPM/1bsTvsqrZxpvZ3ISBPZlsMg7pxLrPWxw==
Source133:      https://registry.npmjs.org/@girs/gobject-2.0/-/gobject-2.0-4.1.0.tgz
%define         SHA512SUM133 5hPKlUOe8WdFQ6/uMS/0FEKC60ZNNJryIv9Qd4QB1jJkTHiah9TSQH4QVZNF14lQDxxYjAIgY8mcchGL2+bteA==
Source134:      https://registry.npmjs.org/@girs/graphene-1.0/-/graphene-1.0-4.1.0.tgz
%define         SHA512SUM134 fCwGsfj7wryyakZ9RzLT9+LS59nk9IDVd0OEsK15njhGqTEQ0/96MiFHvyVhCnjcU1ifgz/PdY5uGqKnLXth1g==
Source135:      https://registry.npmjs.org/@girs/gsk-4.0/-/gsk-4.0-4.1.0.tgz
%define         SHA512SUM135 wwgerEraNWX/sXiOnh3q2HrCC+kkdh2W8dXbP40eSEMmanIcXe7sC4nyDHSor1mp3y3XPvpS0BdiNfl4fxWx6A==
Source136:      https://registry.npmjs.org/@girs/gtk-3.0/-/gtk-3.0-4.1.0.tgz
%define         SHA512SUM136 UmfXXy7xGTYL67nQ0DWFsQG4+4NZwVNJ0fkYlr9o5QAzQzhEjNmVzt3wGArIAVjwZsXxrXAnTKcPMeZCgNnmTw==
Source137:      https://registry.npmjs.org/@girs/gtk-4.0/-/gtk-4.0-4.1.0.tgz
%define         SHA512SUM137 4stUvqZtBE3Fv6qhPF6yVVNhVgm9M5HD3WqTXEVxN3GmR8GtBTBSORHYPYSURQzfTASaHlctMmfg5II2A/KFVQ==
Source138:      https://registry.npmjs.org/@girs/gvc-1.0/-/gvc-1.0-4.1.0.tgz
%define         SHA512SUM138 L+y6qJUxw5IhrO45UipRrWoUInW1t0zhcHWfpw2ageZVTlEqaSsdk82dNPAElmNqRvcKUZUrgZLwJEWx+A2fUg==
Source139:      https://registry.npmjs.org/@girs/harfbuzz-0.0/-/harfbuzz-0.0-4.1.0.tgz
%define         SHA512SUM139 370ny6RjcbGFRk6/50AFpCPteWgEN1y+2MyLXwSXGV0duJNlHBHOTtnuPTHkv+gGxp+s3/YTaQWa5UGzkVYN8g==
Source140:      https://registry.npmjs.org/@girs/meta-18/-/meta-18-4.1.0.tgz
%define         SHA512SUM140 KjEMVcOK6ny0nxxsdWI5RrxOSuhj7zh6mrH2EttaXbloqaLmbOCc2bhh61P7zjkhpanattuiEB8x+u3JQjj0tQ==
Source141:      https://registry.npmjs.org/@girs/mtk-18/-/mtk-18-4.1.0.tgz
%define         SHA512SUM141 6Jc6i+g/CRbjskXUw8pwLxfLb4/YVsXrWZy6W4QWgbZzJAxIEZqCBCEhMKSJEcpuyfY382wOpEAGAZCYgHGxrw==
Source142:      https://registry.npmjs.org/@girs/nm-1.0/-/nm-1.0-4.1.0.tgz
%define         SHA512SUM142 ggBoqJ1bBeqWUMkoZTMGgTVVB5FWZk3Wm+bVUzMvrcOEhriS4XiToxvtOZ4SyObvNMaUvYku/pIAADxpVTWacg==
Source143:      https://registry.npmjs.org/@girs/pango-1.0/-/pango-1.0-4.1.0.tgz
%define         SHA512SUM143 hHDkTA1fyEDsfn4z2q8xDszXS3PgAqcKEjpFL4Xy0w70+JGW+704uxdi5qLRsi/wfjo6bc5K1v2pNsg3yYLiCg==
Source144:      https://registry.npmjs.org/@girs/pangocairo-1.0/-/pangocairo-1.0-4.1.0.tgz
%define         SHA512SUM144 F1C18l6cQN8xCz4M+1zarllpMRkpPjlZcYiWVA9lTPDZnyfr47JAZGTBQUo/iayKfABMO1BHxeBJqOP2e87S3g==
Source145:      https://registry.npmjs.org/@girs/polkit-1.0/-/polkit-1.0-4.1.0.tgz
%define         SHA512SUM145 lYyv3udRMc9umEBDCB9YlbVKdaIn/CGxGe7EOxI7HzX0/aMbWMHI6XfhDHYwyrcmnIDD0BviVZxPOaYDXTTimA==
Source146:      https://registry.npmjs.org/@girs/polkitagent-1.0/-/polkitagent-1.0-4.1.0.tgz
%define         SHA512SUM146 RYY7dceP+HQkOAaCM3uucmLsnnp4lNRxVH4PTxQE/yDt46mG2YjWE+pb7ksoZph4LWcMgaOhUKpLEJdNtULLRQ==
Source147:      https://registry.npmjs.org/@girs/shell-18/-/shell-18-4.1.0.tgz
%define         SHA512SUM147 AGFHEDHTeYryprLkhYZdQTQVrbIgpA0qJTvXDnN+aeIL5wE34OBI9/GjxnQM34i6r/3t1uiDkgYeElOQ54vH1A==
Source148:      https://registry.npmjs.org/@girs/shew-0/-/shew-0-4.1.0.tgz
%define         SHA512SUM148 ErZ+tzi9SQBHIqOD+Arprk7iFw8cweQmp2aXQe4yol2i6cj8VbSow2OinjgBBJzoHGyPCKCuIQLzjDEzTWKIig==
Source149:      https://registry.npmjs.org/@girs/st-18/-/st-18-4.1.0.tgz
%define         SHA512SUM149 Ki/B94KToCbl19nU3q1RaPcwU2X3jswBXZhSRFA+8envBdFRWvXaIxEyB9rL9dK5TlO17/MygdCc3cdBmmc4jA==
Source150:      https://registry.npmjs.org/@girs/upowerglib-1.0/-/upowerglib-1.0-4.1.0.tgz
%define         SHA512SUM150 GLLY6HiRPD0LainaJc442l3Vf/vSu2cii5IYK36BvGjOSx712cp5d4/Xb80a/TA9/Jrbqr3tO8j8rzNjGRrmAw==
Source151:      https://registry.npmjs.org/@girs/xfixes-4.0/-/xfixes-4.0-4.1.0.tgz
%define         SHA512SUM151 WiS3TneSclpsUHcgXsU5Gj3LOcxiYeT8h2FM4PbOVarOGfMMNTdxDWp3kJdRuuUboKaepLCGSZY3MN53YtT6jA==
Source152:      https://registry.npmjs.org/@girs/xlib-2.0/-/xlib-2.0-4.1.0.tgz
%define         SHA512SUM152 dLV0ObD16/+909MXi41ccYZqeh5G8uvi4uSzaX4H++kgOOA0D81PBacPjxLEEGizbLw/rzf46elwy6OHyjc/8Q==
Source153:      https://registry.npmjs.org/@humanfs/core/-/core-0.19.2.tgz
%define         SHA512SUM153 UhXNm+CFMWcbChXywFwkmhqjs3PRCmcSa/hfBgLIb7oQ5HNb1wS0icWsGtSAUNgefHeI+eBrA8I1fxmbHsGdvA==
Source154:      https://registry.npmjs.org/@humanfs/node/-/node-0.16.8.tgz
%define         SHA512SUM154 gE1eQNZ3R++kTzFUpdGlpmy8kDZD/MLyHqDwqjkVQI0JMdI1D51sy1H958PNXYkM2rAac7e5/CnIKZrHtPh3BQ==
Source155:      https://registry.npmjs.org/@humanfs/types/-/types-0.15.0.tgz
%define         SHA512SUM155 ZZ1w0aoQkwuUuC7Yf+7sdeaNfqQiiLcSRbfI08oAxqLtpXQr9AIVX7Ay7HLDuiLYAaFPu8oBYNq/QIi9URHJ3Q==
Source156:      https://registry.npmjs.org/@humanwhocodes/module-importer/-/module-importer-1.0.1.tgz
%define         SHA512SUM156 bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==
Source157:      https://registry.npmjs.org/@humanwhocodes/retry/-/retry-0.4.3.tgz
%define         SHA512SUM157 bV0Tgo9K4hfPCek+aMAn81RppFKv2ySDQeMoSZuvTASywNTnVJCArCZE2FWqpvIatKu7VMRLWlR1EazvVhDyhQ==
Source158:      https://registry.npmjs.org/@types/esrecurse/-/esrecurse-4.3.1.tgz
%define         SHA512SUM158 xJBAbDifo5hpffDBuHl0Y8ywswbiAp/Wi7Y/GtAgSlZyIABppyurxVueOPE8LUQOxdlgi6Zqce7uoEpqNTeiUw==
Source159:      https://registry.npmjs.org/@types/estree/-/estree-1.0.9.tgz
%define         SHA512SUM159 GhdPgy1el4/ImP05X05Uw4cw2/M93BCUmnEvWZNStlCzEKME4Fkk+YpoA5OiHNQmoS7Cafb8Xa3Pya8m1Qrzeg==
Source160:      https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz
%define         SHA512SUM160 5+fP8P8MFNC+AyZCDxrB2pkZFPGzqQWUzpSeuuVLvm8VMcorNYavBqoFcxK8bQz4Qsbn4oUEEem4wDLfcysGHA==
Source161:      https://registry.npmjs.org/@typescript-eslint/eslint-plugin/-/eslint-plugin-8.68.0.tgz
%define         SHA512SUM161 WASHDpCm6qO5jj9g1a+8NiW5+GCkAyLReR56/4VruYmNgfUmqpxOfZ2Yfb8xGfJPWv5Qi6LSD8sXdces3vbp/Q==
Source162:      https://registry.npmjs.org/ignore/-/ignore-7.0.6.tgz
%define         SHA512SUM162 BAg6QkE8W+TuQLrrw0Ugr7HegXduRuuj8/ti2kSOc+jz1dmx8/WNcjr6XGnq5YpDWxFwwaavqD0+jIUOKelTsw==
Source163:      https://registry.npmjs.org/@typescript-eslint/parser/-/parser-8.68.0.tgz
%define         SHA512SUM163 fHq2VC1kpyYfvEcbiMjOpySY4WS7voEp89yAThrHRX5sm9j2lzYppCb2umFMEed4fWcyeLjHxrz0mpjNBaBxMQ==
Source164:      https://registry.npmjs.org/@typescript-eslint/project-service/-/project-service-8.68.0.tgz
%define         SHA512SUM164 5GQtWZCXFcFYux955pvoS02WLc49pXNlvIxocKjS0clvwo3in1RdlzVKyiqQH9vE5AKWFLTaUgeQkOrTS+0Qxw==
Source165:      https://registry.npmjs.org/@typescript-eslint/scope-manager/-/scope-manager-8.68.0.tgz
%define         SHA512SUM165 T5eXpcaJNg8bhjHJ8Rjp68Vq/QBteYtTKY8TZqVNPaUbuz0f6jI9t6aDkylwvalpAB9XTTFeFOjrjXAZ3YvmVA==
Source166:      https://registry.npmjs.org/@typescript-eslint/tsconfig-utils/-/tsconfig-utils-8.68.0.tgz
%define         SHA512SUM166 F7zrGQfiJHojPwi8vhxZQC1tWtJzvL74cK/nqri2lk8YUXvYaYwl263xOJ69jDWPUk1hmcdoayFwk9lX09npVw==
Source167:      https://registry.npmjs.org/@typescript-eslint/type-utils/-/type-utils-8.68.0.tgz
%define         SHA512SUM167 X77zqoY1EjeWGs/0JNxeaMfp5C5lIz4Tw8y66F1Ne8Faq6g424sBNYM6xBAqElfGZPLpWS+CZAp0DXyKDzWiHg==
Source168:      https://registry.npmjs.org/@typescript-eslint/types/-/types-8.68.0.tgz
%define         SHA512SUM168 9RnpsGJjrAllCMefGVVsImJM24YurhC0Q1h4UbvivtvOqXmR/vEJge2OoE++z9m6hyg8T1Q8t5SNT6tHSbrxcg==
Source169:      https://registry.npmjs.org/@typescript-eslint/typescript-estree/-/typescript-estree-8.68.0.tgz
%define         SHA512SUM169 OKKsD0tYmoNiU5PW2zehO1yO56jYOm1ShYlxon/Z0SJNidAkdVg86eg9ruRuoXf8xfnuWZGbwDsStkoXbZtIIA==
Source170:      https://registry.npmjs.org/@typescript-eslint/utils/-/utils-8.68.0.tgz
%define         SHA512SUM170 PB5gJMMOg0Q5P1tsgWtEAqQacJXq0qEqRHDX/YJ4FaTMLfZPpHB3gjl2EJuiZyPABxmj4ZQYiY9m1bdAJ5y7tQ==
Source171:      https://registry.npmjs.org/@typescript-eslint/visitor-keys/-/visitor-keys-8.68.0.tgz
%define         SHA512SUM171 YR65gGdGvTUAWLldC3xLOvOzamdGzB4A5/N8rehEaHs3Zvoe39BhgY+u0SPch1OvrVTfLcc55wsSgK2NcnTS/A==
Source172:      https://registry.npmjs.org/typescript/-/typescript-7.0.2.tgz
%define         SHA512SUM172 8FYau96o3NKOhbjKi/qNvG/W5jhzxkbdm5sj9AbZ/5T5sWqn3hJgLfGx27sRKZWTvyzCP8dLRBTf5tBTSRVUNA==
Source173:      https://registry.npmjs.org/typescript/-/typescript-6.0.3.tgz
%define         SHA512SUM173 y2TvuxSZPDyQakkFRPZHKFm+KKVqIisdg9/CZwm9ftvKXLP8NRWj38/ODjNbr43SsoXqNuAisEf1GdCxqWcdBw==
Source174:      https://registry.npmjs.org/@typescript/typescript-linux-arm/-/typescript-linux-arm-7.0.2.tgz
%define         SHA512SUM174 gffT3xPz9sR7j/YJExkyPntrI0P2EP9XbOyWzth2/Gs0RstK+90RBcO0ncXoXy/beYll1SXw846Nf2zdnEz0QQ==
Source175:      https://registry.npmjs.org/@typescript/typescript-linux-arm64/-/typescript-linux-arm64-7.0.2.tgz
%define         SHA512SUM175 Qh4eU4/y3yDjnfjjyPYihMj5/ODIlmt+Bzu17OI+fiSRDW57QmU5SiN63exPRNJPKUzcc1INa1NXdrJ+MqHjUQ==
Source176:      https://registry.npmjs.org/@typescript/typescript-linux-loong64/-/typescript-linux-loong64-7.0.2.tgz
%define         SHA512SUM176 uEHck9i8hoAzXPiYRib1O7miOnz23SxIeVl6F4LXox+qov1K35jHcEW6VHKvZI+pyvl7fZEP4MCU5LYvIq1GuQ==
Source177:      https://registry.npmjs.org/@typescript/typescript-linux-mips64el/-/typescript-linux-mips64el-7.0.2.tgz
%define         SHA512SUM177 R4KvAMnE43W5Qeqb0Ly56O3mWMWIAgsMyz36DCaycd5nbg/9kzm0liw3JocfRqyJY0KPmzFjbswozXyW0DnIYA==
Source178:      https://registry.npmjs.org/@typescript/typescript-linux-ppc64/-/typescript-linux-ppc64-7.0.2.tgz
%define         SHA512SUM178 DORx5b3sd/4S7eayxm4FQv+A7CrkUIGRaHiwI8oiHTAI1fAPWhF4J0vAlkC8biAlHSVVwxMQ3tjZ2/DVbnQiiA==
Source179:      https://registry.npmjs.org/@typescript/typescript-linux-riscv64/-/typescript-linux-riscv64-7.0.2.tgz
%define         SHA512SUM179 wf0jqEDOjrPRnKwYRyyJDRo11KMbvMFrU+q4zqKyChODBzvlkbhNQfKvLxQCcwTpdDaXSHZTVuh0JoCrKCUMHQ==
Source180:      https://registry.npmjs.org/@typescript/typescript-linux-s390x/-/typescript-linux-s390x-7.0.2.tgz
%define         SHA512SUM180 IkwJc3L7yhytWd/ewjyxNDfOmswCm9GWMJT/ue/dU4aZNbwZeYAetq42VyLmsmSjvoX7z74X6ZaYCtzAr0EuGw==
Source181:      https://registry.npmjs.org/@typescript/typescript-linux-x64/-/typescript-linux-x64-7.0.2.tgz
%define         SHA512SUM181 EYdf2cNg7rgCWJnxCdJ+F3V39O8ihb37eHAu1LK8oAFizgTQbPOK7zHHXbPt8rX24COqODXeI3sIf0fCXG7H/A==
Source182:      https://registry.npmjs.org/acorn/-/acorn-8.18.0.tgz
%define         SHA512SUM182 lGq+9yr1/GuAWaVYIHRjvvySG5/4VfKIvC8EWxStPdcDh/Ka7FG3twP6v4d5BkravUilhIAsG4Qj83t02LWUPQ==
Source183:      https://registry.npmjs.org/acorn-jsx/-/acorn-jsx-5.3.2.tgz
%define         SHA512SUM183 rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==
Source184:      https://registry.npmjs.org/ajv/-/ajv-6.15.0.tgz
%define         SHA512SUM184 fgFx7Hfoq60ytK2c7DhnF8jIvzYgOMxfugjLOSMHjLIPgenqa7S7oaagATUq99mV6IYvN2tRmC0wnTYX6iPbMw==
Source185:      https://registry.npmjs.org/balanced-match/-/balanced-match-4.0.4.tgz
%define         SHA512SUM185 BLrgEcRTwX2o6gGxGOCNyMvGSp35YofuYzw9h1IMTRmKqttAZZVU67bdb9Pr2vUHA8+j3i2tJfjO6C6+4myGTA==
Source186:      https://registry.npmjs.org/brace-expansion/-/brace-expansion-5.0.9.tgz
%define         SHA512SUM186 ScQ4IuvIEF1TMlP7Zt+vjJ//9zlPb2SDcxWxM3bk8s6t6GGdJ7KO1dCcTidOPJKePW30LE/2cT7wCyPho9/Wxg==
Source187:      https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz
%define         SHA512SUM187 uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==
Source188:      https://registry.npmjs.org/debug/-/debug-4.4.3.tgz
%define         SHA512SUM188 RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==
Source189:      https://registry.npmjs.org/deep-is/-/deep-is-0.1.4.tgz
%define         SHA512SUM189 oIPzksmTg4/MriiaYGO+okXDT7ztn/w3Eptv/+gSIdMdKsJo0u4CfYNFJPy+4SKMuCqGw2wxnA+URMg3t8a/bQ==
Source190:      https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-4.0.0.tgz
%define         SHA512SUM190 TtpcNJ3XAzx3Gq8sWRzJaVajRs0uVxA2YAkdb1jm2YkPz4G6egUFAyA3n5vtEIZefPk5Wa4UXbKuS5fKkJWdgA==
Source191:      https://registry.npmjs.org/eslint/-/eslint-10.9.1.tgz
%define         SHA512SUM191 9VaAkDURekixUQJy0oJYl2DcN6oKMfxay7XzaGYAWQwsb6qfKf+x76R2k1L8kb1boc+FyCAaTA9GmiKaaiaF+A==
Source192:      https://registry.npmjs.org/eslint-scope/-/eslint-scope-9.1.2.tgz
%define         SHA512SUM192 xS90H51cKw0jltxmvmHy2Iai1LIqrfbw57b79w/J7MfvDfkIkFZ+kj6zC3BjtUwh150HsSSdxXZcsuv72miDFQ==
Source193:      https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-5.0.1.tgz
%define         SHA512SUM193 tD40eHxA35h0PEIZNeIjkHoDR4YjjJp34biM0mDvplBe//mB+IHCqHDGV7pxF+7MklTvighcCPPZC7ynWyjdTA==
Source194:      https://registry.npmjs.org/espree/-/espree-11.2.0.tgz
%define         SHA512SUM194 7p3DrVEIopW1B1avAGLuCSh1jubc01H2JHc8B4qqGblmg5gI9yumBgACjWo4JlIc04ufug4xJ3SQI8HkS/Rgzw==
Source195:      https://registry.npmjs.org/esquery/-/esquery-1.7.0.tgz
%define         SHA512SUM195 Ap6G0WQwcU/LHsvLwON1fAQX9Zp0A2Y6Y/cJBl9r/JbW90Zyg4/zbG6zzKa2OTALELarYHmKu0GhpM5EO+7T0g==
Source196:      https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz
%define         SHA512SUM196 KmfKL3b6G+RXvP8N1vr3Tq1kL/oCFgn2NYXEtqP8/L3pKapUA4G8cFVaoF3SU323CD4XypR/ffioHmkti6/Tag==
Source197:      https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz
%define         SHA512SUM197 MMdARuVEQziNTeJD8DgMqmhwR11BRQ/cBP+pLtYdSTnf3MIO8fFeiINEbX36ZdNlfU/7A9f3gUw49B3oQsvwBA==
Source198:      https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
%define         SHA512SUM198 kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g==
Source199:      https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
%define         SHA512SUM199 f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==
Source200:      https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
%define         SHA512SUM200 lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==
Source201:      https://registry.npmjs.org/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz
%define         SHA512SUM201 DCXu6Ifhqcks7TZKY3Hxp3y6qphY5SJZmrWMDrKcERSOXWQdMhU9Ig/PYrzyw/ul9jOIyh0N4M0tbC5hodg8dw==
Source202:      https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz
%define         SHA512SUM202 tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==
Source203:      https://registry.npmjs.org/file-entry-cache/-/file-entry-cache-8.0.0.tgz
%define         SHA512SUM203 XXTUwCvisa5oacNGRP9SfNtYBNAMi+RPwBFmblZEF7N7swHYQS6/Zfk7SRwx4D5j3CH211YNRco1DEMNVfZCnQ==
Source204:      https://registry.npmjs.org/find-up/-/find-up-5.0.0.tgz
%define         SHA512SUM204 78/PXT1wlLLDgTzDs7sjq9hzz0vXD+zn+7wypEe4fXQxCmdmqfGsEPQxmiCSQI3ajFV91bVSsvNtrJRiW6nGng==
Source205:      https://registry.npmjs.org/flat-cache/-/flat-cache-4.0.1.tgz
%define         SHA512SUM205 f7ccFPK3SXFHpx15UIGyRJ/FJQctuKZ0zVuN3frBo4HnK3cay9VEW0R6yPYFHC0AgqhukPzKjq22t5DmAyqGyw==
Source206:      https://registry.npmjs.org/flatted/-/flatted-3.4.4.tgz
%define         SHA512SUM206 5+ybhBZANEJxaH3X5evAFatUxLfEHSr7n6kYJ+1Qd0mUqr4eu9gIf6GDbWHf8RJijHrjjO8G+la14SlL2SeS1Q==
Source207:      https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz
%define         SHA512SUM207 XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==
Source208:      https://registry.npmjs.org/ignore/-/ignore-5.3.2.tgz
%define         SHA512SUM208 hsBTNUqQTDwkWtcdYI2i06Y/nUBEsNEDJKjWdigLvegy8kDuJAS8uRlpkkcQpyEXL0Z/pjDy5HBmMjRCJ2gq+g==
Source209:      https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz
%define         SHA512SUM209 JmXMZ6wuvDmLiHEml9ykzqO6lwFbof0GG4IkcGaENdCRDDmMVnny7s5HsIgHCbaq0w2MyPhDqkhTUgS2LU2PHA==
Source210:      https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz
%define         SHA512SUM210 SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==
Source211:      https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz
%define         SHA512SUM211 xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==
Source212:      https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
%define         SHA512SUM212 RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==
Source213:      https://registry.npmjs.org/json-buffer/-/json-buffer-3.0.1.tgz
%define         SHA512SUM213 4bV5BfR2mqfQTJm+V5tPPdf+ZpuhiIvTuAB5g8kcrXOZpTT/QwwVRWBywX1ozr6lEuPdbHxwaJlm9G6mI2sfSQ==
Source214:      https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
%define         SHA512SUM214 xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg==
Source215:      https://registry.npmjs.org/json-stable-stringify-without-jsonify/-/json-stable-stringify-without-jsonify-1.0.1.tgz
%define         SHA512SUM215 Bdboy+l7tA3OGW6FjyFHWkP5LuByj1Tk33Ljyq0axyzdk9//JSi2u3fP1QSmd1KNwq6VOKYGlAu87CisVir6Pw==
Source216:      https://registry.npmjs.org/keyv/-/keyv-4.5.4.tgz
%define         SHA512SUM216 oxVHkHR/EJf2CNXnWxRLW6mg7JyCCUcG0DtEGmL2ctUo1PNTin1PUil+r/+4r5MpVgC/fn1kjsx7mjSujKqIpw==
Source217:      https://registry.npmjs.org/levn/-/levn-0.4.1.tgz
%define         SHA512SUM217 +bT2uH4E5LGE7h/n3evcS/sQlJXCpIp6ym8OWJ5eV6+67Dsql/LaaT7qJBAt2rzfoa/5QBGBhxDix1dMt2kQKQ==
Source218:      https://registry.npmjs.org/locate-path/-/locate-path-6.0.0.tgz
%define         SHA512SUM218 iPZK6eYjbxRu3uB4/WZ3EsEIMJFMqAoopl3R+zuq0UjcAm/MO6KCweDgPfP3elTztoKP3KtnVHxTn2NHBSDVUw==
Source219:      https://registry.npmjs.org/minimatch/-/minimatch-10.2.6.tgz
%define         SHA512SUM219 vpLQEs+VLCr1nU0BXS07maYoFwlDAH0gngQuuttxIwutDFEMHq2blX+8vpgxDdK3J1PwjCJiep77OitTZ4Ll1A==
Source220:      https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
%define         SHA512SUM220 6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==
Source221:      https://registry.npmjs.org/natural-compare/-/natural-compare-1.4.0.tgz
%define         SHA512SUM221 OWND8ei3VtNC9h7V60qff3SVobHr996CTwgxubgyQYEpg290h9J0buyECNNJexkFm5sOajh5G116RYA1c8ZMSw==
Source222:      https://registry.npmjs.org/optionator/-/optionator-0.9.4.tgz
%define         SHA512SUM222 6IpQ7mKUxRcZNLIObR0hz7lxsapSSIYNZJwXPGeF0mTVqGKFIXj1DQcMoT22S3ROcLyY/rz0PWaWZ9ayWmad9g==
Source223:      https://registry.npmjs.org/p-limit/-/p-limit-3.1.0.tgz
%define         SHA512SUM223 TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==
Source224:      https://registry.npmjs.org/p-locate/-/p-locate-5.0.0.tgz
%define         SHA512SUM224 LaNjtRWUBY++zB5nE/NwcaoMylSPk+S+ZHNB1TzdbMJMny6dynpAGt7X/tl/QYq3TIeE6nxHppbo2LGymrG5Pw==
Source225:      https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz
%define         SHA512SUM225 ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w==
Source226:      https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz
%define         SHA512SUM226 ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==
Source227:      https://registry.npmjs.org/picomatch/-/picomatch-4.0.7.tgz
%define         SHA512SUM227 qcJu88Q2IWqJsDD529JKMdwGm/dvInW4HvQnRwiH9JtihJvzGOscDtHE3x1pBKeUOTysQ8kVmLnJ2kJu7yhcGA==
Source228:      https://registry.npmjs.org/prelude-ls/-/prelude-ls-1.2.1.tgz
%define         SHA512SUM228 vkcDPrRZo1QZLbn5RLGPpg/WmIQ65qoWWhcGKf/b5eplkkarX0m9z8ppCat4mlOqUsWpyNuYgO3VRyrYHSzX5g==
Source229:      https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz
%define         SHA512SUM229 vYt7UD1U9Wg6138shLtLOvdAu+8DsC/ilFtEVHcH+wydcSpNE20AfSOduf6MkRFahL5FY7X1oU7nKVZFtfq8Fg==
Source230:      https://registry.npmjs.org/semver/-/semver-7.8.5.tgz
%define         SHA512SUM230 Y7/KDsb8LjooZpwaqGyulO6DQlksgCncchHGk+sZIY4SBvUocMBEFH5Ur1fI4dV+Jvl0w6cjvucaIi40puRioA==
Source231:      https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz
%define         SHA512SUM231 kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==
Source232:      https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz
%define         SHA512SUM232 7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==
Source233:      https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.17.tgz
%define         SHA512SUM233 wXR/dYpcqKmfWpEdZjiKJOwCNFndD0DMnrW/cYjVGttEkBfVgcLFHoNrlj47mjOVic9yyNu65alsgF4NQyTa2g==
Source234:      https://registry.npmjs.org/ts-api-utils/-/ts-api-utils-2.5.0.tgz
%define         SHA512SUM234 OJ/ibxhPlqrMM0UiNHJ/0CKQkoKF243/AEmplt3qpRgkW8VG7IfOS41h7V8TjITqdByHzrjcS/2si+y4lIh8NA==
Source235:      https://registry.npmjs.org/type-check/-/type-check-0.4.0.tgz
%define         SHA512SUM235 XleUoc9uwGXqjWwXaUTZAmzMcFZ5858QA2vvx1Ur5xIcixXIP+8LnFDgRplU30us6teqdlskFfu+ae4K79Ooew==
Source236:      https://registry.npmjs.org/@typescript/typescript6/-/typescript6-6.0.2.tgz
%define         SHA512SUM236 mbCddXd+jm7hfx7w2YU64/Av4/NqqeG3GoRZgxPcgoTxYjhrcfJRw9ULch71SS4G+Q3bOXFhRvPqjguN0Hyp5w==
Source237:      https://registry.npmjs.org/typescript-eslint/-/typescript-eslint-8.68.0.tgz
%define         SHA512SUM237 MHy0Y0ynqeEbx/S45+i/bBssdy3X6KNBfmJAP35GrgtNxu2TQ5K5xsFDhAnmsq1jvpdoZOPG1LGtJo0HWqYCrQ==
Source238:      https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
%define         SHA512SUM238 7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==
Source239:      https://registry.npmjs.org/which/-/which-2.0.2.tgz
%define         SHA512SUM239 BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==
Source240:      https://registry.npmjs.org/word-wrap/-/word-wrap-1.2.5.tgz
%define         SHA512SUM240 BN22B5eaMMI9UMtjrGd5g5eCYPpCPDUy0FJXbYsaT5zYxjFOckS53SQDE3pWkVoWpHXVb3BrYcEN4Twa55B5cA==
Source241:      https://registry.npmjs.org/yocto-queue/-/yocto-queue-0.1.0.tgz
%define         SHA512SUM241 rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==
# END NPM SOURCES

BuildRequires:  nodejs-devel
BuildRequires:  nodejs22-npm
BuildRequires:  make

Requires:       gnome-shell >= 45
Recommends:     gnome-extensions-app
Recommends:     %{name}-shortcut-overrides = %{version}-%{release}
Provides:       %{extension} = %{version}-%{release}


%description
Pop Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows.  The core feature of Pop Shell
is the addition of advanced tiling window management - a feature that has been
highly sought within our community.  For many - ourselves included - i3wm has
become the leading competitor to the GNOME desktop.


%package shortcut-overrides
Summary:        Shortcut overrides for %{name}


%description shortcut-overrides
Shortcut overrides for %{name}.


%prep
%autosetup -p 1 -n pop-shell-%{commit}
for f in %{_sourcedir}/*.tgz; do
  npm cache add "$f"
done


%build
%make_build compile


%install
# install main extension files
%make_install

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install the gnome-control-center keybindings
install -d -m 0755 %{buildroot}%{_datadir}/gnome-control-center/keybindings
install -p -m 0644 keybindings/*.xml %{buildroot}%{_datadir}/gnome-control-center/keybindings/

# install the schema override files
install -d -m 0755 %{buildroot}%{_datadir}/glib-2.0/schemas
install -p -m 0644 %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{buildroot}%{_datadir}/glib-2.0/schemas/


%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml


%files shortcut-overrides
%{_datadir}/glib-2.0/schemas/*.%{extension}.gschema.override


%changelog
%autochangelog
