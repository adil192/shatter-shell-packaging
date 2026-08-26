%global extension   pop-shell
%global uuid        %{extension}@system76.com
%global commit      453f755a55991dc1dde4b7a09e0331f12f816b35
%global shortcommit %{sub %{commit} 1 7}

Name:           gnome-shell-extension-%{extension}
Version:        1.2.0^31.%{shortcommit}
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
Source101:      https://registry.npmjs.org/@girs/accountsservice-1.0/-/accountsservice-1.0-4.1.0.tgz
%define         SHA512SUM101 Kp8TXbun34nQJ6h0EOqmAJ8P8sd3huzJMPtdw2FOpTPzViFcUPC95fICi231Ur0FhfhH62lXZnHthifUKb01HQ==
Source102:      https://registry.npmjs.org/@girs/adw-1/-/adw-1-4.1.0.tgz
%define         SHA512SUM102 Xv4doRXq7o9K+plUlrjl7e6ba04jtc7JS6U8JEMGZuNOL0BXsZa2lNbnLKKjUQnwzbh80EDECgyhiBkbhq7Heg==
Source103:      https://registry.npmjs.org/@girs/atk-1.0/-/atk-1.0-4.1.0.tgz
%define         SHA512SUM103 GBf3Ehc56boCbDx9lOt4hMWaETgxsUZ33Bfk022BVHhvWwXd5iWFt9wQHTiFkgJcAJjmPavhkouniAbuuBwH4Q==
Source104:      https://registry.npmjs.org/@girs/cairo-1.0/-/cairo-1.0-4.1.0.tgz
%define         SHA512SUM104 iCdRmpCPpQn+skaJfLsDUvSSidKgQLAsFeah5Ac5I5dRmpdwCvDTsox6wreZssfhERWcUAldtWj7wXmSzPBLKg==
Source105:      https://registry.npmjs.org/@girs/clutter-18/-/clutter-18-4.1.0.tgz
%define         SHA512SUM105 1peMQVW/Uu22YoEG8Msx8lRQgOXy1Efuw2al03v6Lc0yWdAXdL8aWZ4d8p6YKAH6WTBmiMthWG60+bZqKur0Cw==
Source106:      https://registry.npmjs.org/@girs/cogl-18/-/cogl-18-4.1.0.tgz
%define         SHA512SUM106 eykux7piDFKlAoNpuEdzi7FjrD3TbSNlGCUHgKkkV8NEgU0WQr+SH15yCVMJDlqR4cxH8byESOaiXginEBIgEg==
Source107:      https://registry.npmjs.org/@girs/freetype2-2.0/-/freetype2-2.0-4.1.0.tgz
%define         SHA512SUM107 /+fMzCY84TrKi5wcT/EVQulM9xPhCAA5cTaZclzufA01MvasA8vrPu5zEF8qhfYbm77ro94A8P6kWpcOf1LxEQ==
Source108:      https://registry.npmjs.org/@girs/gck-2/-/gck-2-4.1.0.tgz
%define         SHA512SUM108 jrFH1iWhkGxFG2jCS+NYzWBM6jcaNYNysA3r9AT+EWmY7kVkMeGi9ec+LSqIqjC0qU/MaHaLIZ6HU6o34zZU3Q==
Source109:      https://registry.npmjs.org/@girs/gcr-4/-/gcr-4-4.1.0.tgz
%define         SHA512SUM109 gpwN7hDZDg7ZFvVKhQcRIm5BhmcprFigtn6NR5Kohsquc6YGiq70v9Xo19gmWRQMFMo3nB+mZAAjzvTbpXhCww==
Source110:      https://registry.npmjs.org/@girs/gdesktopenums-3.0/-/gdesktopenums-3.0-4.1.0.tgz
%define         SHA512SUM110 itkzeTHIezAVpuQgqDPKPPt00KOUZRPPdQBU4Ac/4/nKZTcmKwPFfLgQjgkcX1V4UQYknvGFoEY2E8X2tJagiQ==
Source111:      https://registry.npmjs.org/@girs/gdk-3.0/-/gdk-3.0-4.1.0.tgz
%define         SHA512SUM111 CFDjHJ7frLtqZXLLFnqeCGfPOyPrzlX3g8sAAhWJnjrqPShEXmFuXXOOOyZfQXcxynHTIx0rPSOiujH9ZNSTHw==
Source112:      https://registry.npmjs.org/@girs/gdk-4.0/-/gdk-4.0-4.1.0.tgz
%define         SHA512SUM112 Wf7ZaDS2e+DUJwEBVn/DQux42b2KQYNhWeaheK7nx5Ia6Y/w3Xpm/yqqYJh+KnZ+y8IgypjpscjL4qBkr944rw==
Source113:      https://registry.npmjs.org/@girs/gdkpixbuf-2.0/-/gdkpixbuf-2.0-4.1.0.tgz
%define         SHA512SUM113 i89aPIgZPSD1/UNH5PlsT7660HtqfPu8eU5TeSedUV7H5kCWXRO11SqbRpGJoa3ScMu8UU0LOkgFB1f1x0QefA==
Source114:      https://registry.npmjs.org/@girs/gdm-1.0/-/gdm-1.0-4.1.0.tgz
%define         SHA512SUM114 JwIbQx1ABn0FSahUCXFyTrPkF7W38z6wyx2ydW+5ge5j2YKJTmadFd+/vK4BKyJgwkH9IjseLeWXzUrhQurBKQ==
Source115:      https://registry.npmjs.org/@girs/gio-2.0/-/gio-2.0-4.1.0.tgz
%define         SHA512SUM115 irRUpGEOHknlk4TNoOlAaBCg/jCGZKZv8Ulr23mmqf+MTI6ygDcbJY6bdHAf5dZfbgkOXjhXRl753j8F850W9Q==
Source116:      https://registry.npmjs.org/@girs/giounix-2.0/-/giounix-2.0-4.1.0.tgz
%define         SHA512SUM116 e3JbHrw+MDbY4NzgMAIh7OUkA7bRfe8AuivklDPNF4b42q+ROyY2A1FZ+wYWGDYuRcjj8vokgDYIJ9hFy1wbAQ==
Source117:      https://registry.npmjs.org/@girs/gjs/-/gjs-4.1.0.tgz
%define         SHA512SUM117 fF6beHhI/DW/4WF2JVDRVpjnWuae93euyr4NXOOTNXwaatDxbMB21jte+b0+Qc7eUEqjIUhV10Hq6ztl4hKWQg==
Source118:      https://registry.npmjs.org/@girs/gl-1.0/-/gl-1.0-4.1.0.tgz
%define         SHA512SUM118 DO2ibBPLGJe9IRWjQQ1zR7bVjk6yBWsvnN1W1fCweNItavJ2+fwTkyo8uHUnYtn5X2FIlx+drkO8VggFnbwdVA==
Source119:      https://registry.npmjs.org/@girs/glib-2.0/-/glib-2.0-4.1.0.tgz
%define         SHA512SUM119 1OeIRobL8UEPP5HXD+lwEgM3643aof+mJ6GJD6TMtzuI9ZbuVyS9MJjQopHW+YrRSLAZwfSQXm2WipA3p3EZmg==
Source120:      https://registry.npmjs.org/@girs/gmodule-2.0/-/gmodule-2.0-4.1.0.tgz
%define         SHA512SUM120 yOFTdnvD61ohMDk12T2Rhcve6vP4/vZpwb/0iQYLu4ZOTD6cazMEdpM+ncZSj8beffbRqTfd7H81HNAriVVm5Q==
Source121:      https://registry.npmjs.org/@girs/gnome-shell/-/gnome-shell-50.0.4.tgz
%define         SHA512SUM121 69phtdJHMPUBxVRDqfE4JWSZeauTIl0zFuILMIkJbqyHOb1U9sxN7yN59x+pJWGxVTktFz/Y9uXKjDzOcHlYFA==
Source122:      https://registry.npmjs.org/@girs/gnomebg-4.0/-/gnomebg-4.0-4.1.0.tgz
%define         SHA512SUM122 9uha/ow4xAEqTiUkd0ew3vRlYTz3YHSG3HMQiGcVYdE/pWHFHjXQ5pToOIyQoDLL+HhoFy7XCUCCBxkgTuSk7w==
Source123:      https://registry.npmjs.org/@girs/gnomebluetooth-3.0/-/gnomebluetooth-3.0-4.1.0.tgz
%define         SHA512SUM123 V0Lo4JE0jotRbXZume/ZpoxUDyX8u1Iw8TD7i26iaMcsTQkNaEJdoNZfhL2WVW1rTU4pwkHD8IGJ2jZLTGInhA==
Source124:      https://registry.npmjs.org/@girs/gnomedesktop-4.0/-/gnomedesktop-4.0-4.1.0.tgz
%define         SHA512SUM124 Rh1kcycDgjI29sjuP+72SODLEqYKxVAZ+FV5DUBmDOVjfNLTlIPPM/1bsTvsqrZxpvZ3ISBPZlsMg7pxLrPWxw==
Source125:      https://registry.npmjs.org/@girs/gobject-2.0/-/gobject-2.0-4.1.0.tgz
%define         SHA512SUM125 5hPKlUOe8WdFQ6/uMS/0FEKC60ZNNJryIv9Qd4QB1jJkTHiah9TSQH4QVZNF14lQDxxYjAIgY8mcchGL2+bteA==
Source126:      https://registry.npmjs.org/@girs/graphene-1.0/-/graphene-1.0-4.1.0.tgz
%define         SHA512SUM126 fCwGsfj7wryyakZ9RzLT9+LS59nk9IDVd0OEsK15njhGqTEQ0/96MiFHvyVhCnjcU1ifgz/PdY5uGqKnLXth1g==
Source127:      https://registry.npmjs.org/@girs/gsk-4.0/-/gsk-4.0-4.1.0.tgz
%define         SHA512SUM127 wwgerEraNWX/sXiOnh3q2HrCC+kkdh2W8dXbP40eSEMmanIcXe7sC4nyDHSor1mp3y3XPvpS0BdiNfl4fxWx6A==
Source128:      https://registry.npmjs.org/@girs/gtk-3.0/-/gtk-3.0-4.1.0.tgz
%define         SHA512SUM128 UmfXXy7xGTYL67nQ0DWFsQG4+4NZwVNJ0fkYlr9o5QAzQzhEjNmVzt3wGArIAVjwZsXxrXAnTKcPMeZCgNnmTw==
Source129:      https://registry.npmjs.org/@girs/gtk-4.0/-/gtk-4.0-4.1.0.tgz
%define         SHA512SUM129 4stUvqZtBE3Fv6qhPF6yVVNhVgm9M5HD3WqTXEVxN3GmR8GtBTBSORHYPYSURQzfTASaHlctMmfg5II2A/KFVQ==
Source130:      https://registry.npmjs.org/@girs/gvc-1.0/-/gvc-1.0-4.1.0.tgz
%define         SHA512SUM130 L+y6qJUxw5IhrO45UipRrWoUInW1t0zhcHWfpw2ageZVTlEqaSsdk82dNPAElmNqRvcKUZUrgZLwJEWx+A2fUg==
Source131:      https://registry.npmjs.org/@girs/harfbuzz-0.0/-/harfbuzz-0.0-4.1.0.tgz
%define         SHA512SUM131 370ny6RjcbGFRk6/50AFpCPteWgEN1y+2MyLXwSXGV0duJNlHBHOTtnuPTHkv+gGxp+s3/YTaQWa5UGzkVYN8g==
Source132:      https://registry.npmjs.org/@girs/meta-18/-/meta-18-4.1.0.tgz
%define         SHA512SUM132 KjEMVcOK6ny0nxxsdWI5RrxOSuhj7zh6mrH2EttaXbloqaLmbOCc2bhh61P7zjkhpanattuiEB8x+u3JQjj0tQ==
Source133:      https://registry.npmjs.org/@girs/mtk-18/-/mtk-18-4.1.0.tgz
%define         SHA512SUM133 6Jc6i+g/CRbjskXUw8pwLxfLb4/YVsXrWZy6W4QWgbZzJAxIEZqCBCEhMKSJEcpuyfY382wOpEAGAZCYgHGxrw==
Source134:      https://registry.npmjs.org/@girs/nm-1.0/-/nm-1.0-4.1.0.tgz
%define         SHA512SUM134 ggBoqJ1bBeqWUMkoZTMGgTVVB5FWZk3Wm+bVUzMvrcOEhriS4XiToxvtOZ4SyObvNMaUvYku/pIAADxpVTWacg==
Source135:      https://registry.npmjs.org/@girs/pango-1.0/-/pango-1.0-4.1.0.tgz
%define         SHA512SUM135 hHDkTA1fyEDsfn4z2q8xDszXS3PgAqcKEjpFL4Xy0w70+JGW+704uxdi5qLRsi/wfjo6bc5K1v2pNsg3yYLiCg==
Source136:      https://registry.npmjs.org/@girs/pangocairo-1.0/-/pangocairo-1.0-4.1.0.tgz
%define         SHA512SUM136 F1C18l6cQN8xCz4M+1zarllpMRkpPjlZcYiWVA9lTPDZnyfr47JAZGTBQUo/iayKfABMO1BHxeBJqOP2e87S3g==
Source137:      https://registry.npmjs.org/@girs/polkit-1.0/-/polkit-1.0-4.1.0.tgz
%define         SHA512SUM137 lYyv3udRMc9umEBDCB9YlbVKdaIn/CGxGe7EOxI7HzX0/aMbWMHI6XfhDHYwyrcmnIDD0BviVZxPOaYDXTTimA==
Source138:      https://registry.npmjs.org/@girs/polkitagent-1.0/-/polkitagent-1.0-4.1.0.tgz
%define         SHA512SUM138 RYY7dceP+HQkOAaCM3uucmLsnnp4lNRxVH4PTxQE/yDt46mG2YjWE+pb7ksoZph4LWcMgaOhUKpLEJdNtULLRQ==
Source139:      https://registry.npmjs.org/@girs/shell-18/-/shell-18-4.1.0.tgz
%define         SHA512SUM139 AGFHEDHTeYryprLkhYZdQTQVrbIgpA0qJTvXDnN+aeIL5wE34OBI9/GjxnQM34i6r/3t1uiDkgYeElOQ54vH1A==
Source140:      https://registry.npmjs.org/@girs/shew-0/-/shew-0-4.1.0.tgz
%define         SHA512SUM140 ErZ+tzi9SQBHIqOD+Arprk7iFw8cweQmp2aXQe4yol2i6cj8VbSow2OinjgBBJzoHGyPCKCuIQLzjDEzTWKIig==
Source141:      https://registry.npmjs.org/@girs/st-18/-/st-18-4.1.0.tgz
%define         SHA512SUM141 Ki/B94KToCbl19nU3q1RaPcwU2X3jswBXZhSRFA+8envBdFRWvXaIxEyB9rL9dK5TlO17/MygdCc3cdBmmc4jA==
Source142:      https://registry.npmjs.org/@girs/upowerglib-1.0/-/upowerglib-1.0-4.1.0.tgz
%define         SHA512SUM142 GLLY6HiRPD0LainaJc442l3Vf/vSu2cii5IYK36BvGjOSx712cp5d4/Xb80a/TA9/Jrbqr3tO8j8rzNjGRrmAw==
Source143:      https://registry.npmjs.org/@girs/xfixes-4.0/-/xfixes-4.0-4.1.0.tgz
%define         SHA512SUM143 WiS3TneSclpsUHcgXsU5Gj3LOcxiYeT8h2FM4PbOVarOGfMMNTdxDWp3kJdRuuUboKaepLCGSZY3MN53YtT6jA==
Source144:      https://registry.npmjs.org/@girs/xlib-2.0/-/xlib-2.0-4.1.0.tgz
%define         SHA512SUM144 dLV0ObD16/+909MXi41ccYZqeh5G8uvi4uSzaX4H++kgOOA0D81PBacPjxLEEGizbLw/rzf46elwy6OHyjc/8Q==
Source145:      https://registry.npmjs.org/@typescript/typescript-linux-arm/-/typescript-linux-arm-7.0.2.tgz
%define         SHA512SUM145 gffT3xPz9sR7j/YJExkyPntrI0P2EP9XbOyWzth2/Gs0RstK+90RBcO0ncXoXy/beYll1SXw846Nf2zdnEz0QQ==
Source146:      https://registry.npmjs.org/@typescript/typescript-linux-arm64/-/typescript-linux-arm64-7.0.2.tgz
%define         SHA512SUM146 Qh4eU4/y3yDjnfjjyPYihMj5/ODIlmt+Bzu17OI+fiSRDW57QmU5SiN63exPRNJPKUzcc1INa1NXdrJ+MqHjUQ==
Source147:      https://registry.npmjs.org/@typescript/typescript-linux-loong64/-/typescript-linux-loong64-7.0.2.tgz
%define         SHA512SUM147 uEHck9i8hoAzXPiYRib1O7miOnz23SxIeVl6F4LXox+qov1K35jHcEW6VHKvZI+pyvl7fZEP4MCU5LYvIq1GuQ==
Source148:      https://registry.npmjs.org/@typescript/typescript-linux-mips64el/-/typescript-linux-mips64el-7.0.2.tgz
%define         SHA512SUM148 R4KvAMnE43W5Qeqb0Ly56O3mWMWIAgsMyz36DCaycd5nbg/9kzm0liw3JocfRqyJY0KPmzFjbswozXyW0DnIYA==
Source149:      https://registry.npmjs.org/@typescript/typescript-linux-ppc64/-/typescript-linux-ppc64-7.0.2.tgz
%define         SHA512SUM149 DORx5b3sd/4S7eayxm4FQv+A7CrkUIGRaHiwI8oiHTAI1fAPWhF4J0vAlkC8biAlHSVVwxMQ3tjZ2/DVbnQiiA==
Source150:      https://registry.npmjs.org/@typescript/typescript-linux-riscv64/-/typescript-linux-riscv64-7.0.2.tgz
%define         SHA512SUM150 wf0jqEDOjrPRnKwYRyyJDRo11KMbvMFrU+q4zqKyChODBzvlkbhNQfKvLxQCcwTpdDaXSHZTVuh0JoCrKCUMHQ==
Source151:      https://registry.npmjs.org/@typescript/typescript-linux-s390x/-/typescript-linux-s390x-7.0.2.tgz
%define         SHA512SUM151 IkwJc3L7yhytWd/ewjyxNDfOmswCm9GWMJT/ue/dU4aZNbwZeYAetq42VyLmsmSjvoX7z74X6ZaYCtzAr0EuGw==
Source152:      https://registry.npmjs.org/@typescript/typescript-linux-x64/-/typescript-linux-x64-7.0.2.tgz
%define         SHA512SUM152 EYdf2cNg7rgCWJnxCdJ+F3V39O8ihb37eHAu1LK8oAFizgTQbPOK7zHHXbPt8rX24COqODXeI3sIf0fCXG7H/A==
Source153:      https://registry.npmjs.org/typescript/-/typescript-7.0.2.tgz
%define         SHA512SUM153 8FYau96o3NKOhbjKi/qNvG/W5jhzxkbdm5sj9AbZ/5T5sWqn3hJgLfGx27sRKZWTvyzCP8dLRBTf5tBTSRVUNA==
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
