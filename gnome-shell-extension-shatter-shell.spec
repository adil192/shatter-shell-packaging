%global extension   shatter-shell
%global uuid        %{extension}@adilhanney.com

Name:           gnome-shell-extension-%{extension}
Version:        2.3.0
Release:        %autorelease
Summary:        GNOME Shell extension for advanced tiling window management
License:        GPL-3.0-only
URL:            https://github.com/adil192/shatter-shell
BuildArch:      noarch

Source0:        %{url}/archive/refs/tags/%{version}/%{extension}-%{version}.tar.gz

Source1:        50_org.gnome.desktop.wm.keybindings.%{extension}.gschema.override
Source2:        50_org.gnome.mutter.%{extension}.gschema.override
Source3:        50_org.gnome.mutter.wayland.%{extension}.gschema.override
Source4:        50_org.gnome.settings-daemon.plugins.media-keys.%{extension}.gschema.override
Source5:        50_org.gnome.shell.%{extension}.gschema.override
# downstream-only
Patch:          0001-Remove-schema-handling-from-transpile.sh.patch

# START NPM SOURCES
Source100:      https://registry.npmjs.org/@cacheable/memory/-/memory-2.2.0.tgz
%define         SHA512SUM100 CTLKqLItRCEixEAewD3/j9DB3/o96gpTPD4eJ1v+DGOlxZRZncRQkGYqqnAGCscYd6RNeXfGeiuCphsPtqyIfQ==
Source101:      https://registry.npmjs.org/@cacheable/utils/-/utils-2.5.0.tgz
%define         SHA512SUM101 buipgOVDkkPXNR5+xBpDw7Zk2n1EvU7qBJCNUcL7rhQ//kfpOXPAvQ511Os0vpLYJ1pZnvudNytkQt2hst3wqA==
Source102:      https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.10.1.tgz
%define         SHA512SUM102 cuadcxVFE8sDK6iWJbs8Sn0av2Nrh2QSGQhVlBW9AaAHqHwjWsZHT8LJ4hFGPh7ASBV2deFdM7H/DPjulmh8rg==
Source103:      https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-3.4.3.tgz
%define         SHA512SUM103 wpc+LXeiyiisxPlEkUzU6svyS1frIO3Mgxj1fdy7Pm8Ygzguax2N3Fa/D/ag1WqbOprdI+uY6wMUl8/a2G+iag==
Source104:      https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz
%define         SHA512SUM104 EriSTlt5OC9/7SXkRSCAhfSxxoSUgBm33OH+IkwbdpgoqsSsUg7y3uh+IICI/Qg4BBWr3U2i39RpmycbxMq4ew==
Source105:      https://registry.npmjs.org/@eslint/config-array/-/config-array-0.23.5.tgz
%define         SHA512SUM105 Y3kKLvC1dvTOT+oGlqNQ1XLqK6D1HU2YXPc52NmAlJZbMMWDzGYXMiPRJ8TYD39muD/OTjlZmNJ4ib7dvSrMBA==
Source106:      https://registry.npmjs.org/@eslint/config-helpers/-/config-helpers-0.7.0.tgz
%define         SHA512SUM106 DObd/KKUsU+FaFv4PLxSRenpXfQWmPXXP3pPZ6/K1PCrMu2vQpMDMuQe/BqYeoLcz8ro0bVDF1RxOJgfVEdhUw==
Source107:      https://registry.npmjs.org/@eslint/core/-/core-1.2.1.tgz
%define         SHA512SUM107 MwcE1P+AZ4C6DWlpin/OmOA54mmIZ/+xZuJiQd4SyB29oAJjN30UW9wkKNptW2ctp4cEsvhlLY/CsQ1uoHDloQ==
Source108:      https://registry.npmjs.org/@eslint/js/-/js-10.0.1.tgz
%define         SHA512SUM108 zeR9k5pd4gxjZ0abRoIaxdc7I3nDktoXZk2qOv9gCNWx3mVwEn32VRhyLaRsDiJjTs0xq/T8mfPtyuXu7GWBcA==
Source109:      https://registry.npmjs.org/@eslint/object-schema/-/object-schema-3.0.5.tgz
%define         SHA512SUM109 vqTaUEgxzm+YDSdElad6PiRoX4t8VGDjCtt05zn4nU810UIx/uNEV7/lZJ6KwFThKZOzOxzXy48da+No7HZaMw==
Source110:      https://registry.npmjs.org/@eslint/plugin-kit/-/plugin-kit-0.7.3.tgz
%define         SHA512SUM110 IkO+/KEUvwbVpiURZg+P7zF74z5Jxe0UgJxVni+RtoHQ6IZieXaO02kmadomap/q+l6bc/jdPGGqTjhuZnuz1Q==
Source111:      https://registry.npmjs.org/@girs/accountsservice-1.0/-/accountsservice-1.0-4.9.0.tgz
%define         SHA512SUM111 rhQgMjVqU1/SmYp4LPZt9u0xpyKoQCrFsedmSSlqZkMSQiZ1/G/UnXBn01RTPw3vtFSAZmqLor547GEVKk6x8w==
Source112:      https://registry.npmjs.org/@girs/adw-1/-/adw-1-4.9.0.tgz
%define         SHA512SUM112 aFGYthrzCwsIxtLvoDn6LXVGAxqBhoF/Cdu46MMI6mxy2VTO3dr53QAzA7KqUtHgzD2TTzWwGm8iN1NCiS6cmw==
Source113:      https://registry.npmjs.org/@girs/atk-1.0/-/atk-1.0-4.9.0.tgz
%define         SHA512SUM113 xLLVjyFeCoOIlTW86WmmX+An7h3hc9HT51hQh4J1VjB28BrSIlu4DL5vldIiwEFMUfJAAsTHP0TSeRj1fCrRpw==
Source114:      https://registry.npmjs.org/@girs/cairo-1.0/-/cairo-1.0-4.9.0.tgz
%define         SHA512SUM114 4k48vMxVsHVNFz2Ow/tqtqaImhHBDbVUMy1gTO1+O3Pst2VZs9xHlKZsnsepWTs1NNvR1/ppqCS1MXjfrGr0ag==
Source115:      https://registry.npmjs.org/@girs/clutter-18/-/clutter-18-4.9.0.tgz
%define         SHA512SUM115 sJNixTPIrnB5hR7KyazsuB7QyOOPafh+j3uvXD3sohyxpWNKnhUErWMtAl2umybLRLZfgW9pXVgdirvCPZ87Lg==
Source116:      https://registry.npmjs.org/@girs/cogl-18/-/cogl-18-4.9.0.tgz
%define         SHA512SUM116 p2AEpE7p51Bg85FztwIXbURFFRa+flwrmeiqngj7jMuJ6qbUBdS28TCEHQkruXT4+NTibZPqxm59Q12TNjX9Pw==
Source117:      https://registry.npmjs.org/@girs/freetype2-2.0/-/freetype2-2.0-4.9.0.tgz
%define         SHA512SUM117 WzRbjGI34XPCRZQxf3O6BkycvoZBtgrw+6CKr6/Kt4vtc6Bq6wLNuIClqfFtKmOpcRNSLKt/uCW9IF/vbyl/dg==
Source118:      https://registry.npmjs.org/@girs/gck-2/-/gck-2-4.9.0.tgz
%define         SHA512SUM118 +FZJo134OnlicT+kCBNeyElVTOYlM6MTtsF1MUGHLLjhYhoZ22oFWqZr2Bwfq7iiuRI+Zve2yo0+Syd0ERNWUw==
Source119:      https://registry.npmjs.org/@girs/gcr-4/-/gcr-4-4.9.0.tgz
%define         SHA512SUM119 c/5BjxJ2vVOnQDQWT+iyE+ZkV/zJzm+FCb4J/UqvzEg+xHYo0uUfGY9wzXB2SEQY4KJ7SEA/v76PpE13T7P1iw==
Source120:      https://registry.npmjs.org/@girs/gdesktopenums-3.0/-/gdesktopenums-3.0-4.9.0.tgz
%define         SHA512SUM120 AMfXl0zYrtdvJeRwo7BjoxQm7YnrnJLMY7qYjvkeSudZ3AZNUMrDKVCpxlRaTtloP9TCycMhhdpnk8CRHUf2Tg==
Source121:      https://registry.npmjs.org/@girs/gdk-4.0/-/gdk-4.0-4.9.0.tgz
%define         SHA512SUM121 iWzhHgGqomiLtwbLY49pZ7MpZ40YYRtzjJ9YvXND2zkN56bZMqiXVRhAuHwDqzEbFtM9p/Pd8Q5DB2LrjIRERw==
Source122:      https://registry.npmjs.org/@girs/gdkpixbuf-2.0/-/gdkpixbuf-2.0-4.9.0.tgz
%define         SHA512SUM122 M5TTMRTKuCRJo4JXJGqTnqED+g2rWFfWFuTka9fnY/NRkwF8soZD+LNy2z58JvVPoNeim4Q1xp1NYpNAxQc/qQ==
Source123:      https://registry.npmjs.org/@girs/gdm-1.0/-/gdm-1.0-4.9.0.tgz
%define         SHA512SUM123 ID75rAR7ND7ngpaXn8CwqoPOGJVsvqTTgMhavN3Uzq/46y3WU/GdXAD4r/zEp8NhPn7p0vcbNF+KRKbkcU6Y4A==
Source124:      https://registry.npmjs.org/@girs/gio-2.0/-/gio-2.0-4.9.0.tgz
%define         SHA512SUM124 3n39vbeOmX1CggTz4vTn+xKpa9wpVe39/gLwoBY6kaXE40OLy6xmNQMB6Nhyutj00acb22fDUx81q6UgQ9gvVg==
Source125:      https://registry.npmjs.org/@girs/giounix-2.0/-/giounix-2.0-4.9.0.tgz
%define         SHA512SUM125 OCinDBCoAvDFrXmIWDUYzXG5AMXnzhQH77ua1r81RiXfkzYLVh5mbVavTviE/k0OY+MDqWQUb5zkC2w8vfNkfg==
Source126:      https://registry.npmjs.org/@girs/gjs/-/gjs-4.9.0.tgz
%define         SHA512SUM126 RxEqCV2ANcz1SrF7nh54mUpe9Oq9YA5HuG+5q/pWToULvCr/sKtMbpNSRsAaS/xgpP7y2qGjX68YVhPjk/gHXg==
Source127:      https://registry.npmjs.org/@girs/gl-1.0/-/gl-1.0-4.9.0.tgz
%define         SHA512SUM127 3mYwXT28bx9ZDlMFliC9NucTRqzSEAManl4GhOP9o/mFUi+VieAbAbtkWLVQvIGfiTnietjZPgeI4JcobozgHA==
Source128:      https://registry.npmjs.org/@girs/glib-2.0/-/glib-2.0-4.9.0.tgz
%define         SHA512SUM128 ylAlrPtjVokPumJbbGQUGT1JSLtR6whvzU2DKVEoVO67h2yqZ37TFYBihwtskVf0/BfLNHdpGj2JPS+wMHJfuQ==
Source129:      https://registry.npmjs.org/@girs/gmodule-2.0/-/gmodule-2.0-4.9.0.tgz
%define         SHA512SUM129 vH75DrILqwaSu2TBgoEeiQlJywLpjGGHSFcT+IQA+iiF+91I2Kqi3KHE9AidxpG226HaRvW+ZNWFECdEV4tPVw==
Source130:      https://registry.npmjs.org/@girs/gnome-shell/-/gnome-shell-50.0.4.tgz
%define         SHA512SUM130 69phtdJHMPUBxVRDqfE4JWSZeauTIl0zFuILMIkJbqyHOb1U9sxN7yN59x+pJWGxVTktFz/Y9uXKjDzOcHlYFA==
Source131:      https://registry.npmjs.org/@girs/gnomebg-4.0/-/gnomebg-4.0-4.9.0.tgz
%define         SHA512SUM131 aMveqDMtQ6rR4xAH00Jtgk2diiD0CIzJKwlVeiuYFRXfFC4MnIQIqxvtHGnpA8Xa/nU7LeubWlMatXFVYLzjTg==
Source132:      https://registry.npmjs.org/@girs/gnomebluetooth-3.0/-/gnomebluetooth-3.0-4.9.0.tgz
%define         SHA512SUM132 T2kiFVGwg0+ltmDpuZn08RcZAAgLfT0nPLvGncPAGkw+HQmXVdT4qMt/br3pBQAY0+wLhugTgb8muWJ3df7u5A==
Source133:      https://registry.npmjs.org/@girs/gnomedesktop-4.0/-/gnomedesktop-4.0-4.9.0.tgz
%define         SHA512SUM133 oEdvsFKCNpEGiRYrPcBkPmp9DfQx7/2ZWUUDU9q+1Qjsjv1z+MdCduxov3x1+OhUpXO0RjQZwfmMxO8ZymDJIQ==
Source134:      https://registry.npmjs.org/@girs/gobject-2.0/-/gobject-2.0-4.9.0.tgz
%define         SHA512SUM134 zEkMERp6u2APCkq1mFnkykxDS9Hqsawun0hiJ5L1fyFv0MWMscVvocyunS8zvsSiu2bsIqqj6F2t0qfNNsZIIg==
Source135:      https://registry.npmjs.org/@girs/graphene-1.0/-/graphene-1.0-4.9.0.tgz
%define         SHA512SUM135 8XPKRlHPzUjXekxAzEWUWwcfC5mwEw2WCpzZ7es1rUCRFB8tjSZWGxqMErHN9hLft7Yd5rtXq8DlUrcmLW/PSg==
Source136:      https://registry.npmjs.org/@girs/gsk-4.0/-/gsk-4.0-4.9.0.tgz
%define         SHA512SUM136 UJyrz2OHu2Fu2fbdo9oq4zyIp8XApKWlXfevLxkWndO/xTRL89WDJBzbh7AzdaDXE9MFbaZwdAla5jQ07wAD/g==
Source137:      https://registry.npmjs.org/@girs/gtk-4.0/-/gtk-4.0-4.9.0.tgz
%define         SHA512SUM137 YuAbI8fVdZylJTvKfap8QQdATsB4s4zMcgkGm9Sro+ZwucUA0QAHSczsc/snqVtUvmpZoPOXan5+MKt7nMmPOg==
Source138:      https://registry.npmjs.org/@girs/gvc-1.0/-/gvc-1.0-4.9.0.tgz
%define         SHA512SUM138 3MUHf6ECC1zYQtfY013Yt+Qm7qlHZe0HvO3ldVaY9b2D0IE8467+suy62LjVheUNNOzwvWiCWLkzh24kTVSyVA==
Source139:      https://registry.npmjs.org/@girs/harfbuzz-0.0/-/harfbuzz-0.0-4.9.0.tgz
%define         SHA512SUM139 7DoBhKUSynQxc/E76KZ1yWBd777NU/JPrBtvv5mBnkfBqxz0LwFFuDcn0iYFTKJ51GgyOfJv6dY5AEEP15n/Kg==
Source140:      https://registry.npmjs.org/@girs/meta-18/-/meta-18-4.9.0.tgz
%define         SHA512SUM140 RxE/sMdMv8wBf3BqDEDWGNcCTK2Ifp96WD5eqhpi3N7eqGfV7Jc6yonogX4LDXcRUC35i6s1Ihp25AAKPtCu8w==
Source141:      https://registry.npmjs.org/@girs/mtk-18/-/mtk-18-4.9.0.tgz
%define         SHA512SUM141 np1v0eSs0Rg9Vafw8IR0VRVNaU4rvEztBW35P4AxjvnxQYX1pvb05mwmlM6CvFtgPvdBUc3NkfZ2JutaeFe/kA==
Source142:      https://registry.npmjs.org/@girs/nm-1.0/-/nm-1.0-4.9.0.tgz
%define         SHA512SUM142 /h7siAsQl39e8OC2eDMotMh7QbiXfcgprDFV+YYRHdH3h6PgBrl2wY7sd6y0J9VRoIWD9C+X6XnAcDuC+GU9gw==
Source143:      https://registry.npmjs.org/@girs/pango-1.0/-/pango-1.0-4.9.0.tgz
%define         SHA512SUM143 WxsQXqenTFNkZB24666aZPuE0BJF0ofx9mhLGXJ99ZpR7yyQY9hwuO6XfECYeKcPQV0Wu47vOtEH1lh1i4GZiQ==
Source144:      https://registry.npmjs.org/@girs/pangocairo-1.0/-/pangocairo-1.0-4.9.0.tgz
%define         SHA512SUM144 4h+8a+6HAkVYsOnbh0BBs5fN/GMqMdi6VkU8vKK60+kqeFjTjtAVQE0W0Qc/OJEVP6Jb8eDph8BPHQEn6a06OQ==
Source145:      https://registry.npmjs.org/@girs/polkit-1.0/-/polkit-1.0-4.9.0.tgz
%define         SHA512SUM145 g1aZ9/sMAoDyiq+ofqgZSdstv/pZvI/8Z01tjS8bmMccN1+51pEAWn7sg7hBltNE+92kEEExbDygmMGXNjfD/g==
Source146:      https://registry.npmjs.org/@girs/polkitagent-1.0/-/polkitagent-1.0-4.9.0.tgz
%define         SHA512SUM146 bbvRhp+z7veoNn/G+6dn2eq6OQAebVKQ3feYCd48H2KJIfJ30kbU9oGNnHDpeXzv2ybcepUzACNE1wRNTKgsRg==
Source147:      https://registry.npmjs.org/@girs/shell-18/-/shell-18-4.9.0.tgz
%define         SHA512SUM147 nqoBZlo0BRE3OsKskzCej6Fp09ZWXS3ZvWNeVEiLwvci3KImsIW6AkEv+NrvlUYO3E9UF5aYDHABFNWvHZLZEA==
Source148:      https://registry.npmjs.org/@girs/shew-0/-/shew-0-4.9.0.tgz
%define         SHA512SUM148 fW4pl8JDRll47YQMAmqEUSQDCZhk4scEEvRsvExLGrWc6MygdwRbFA+04ra+zgRO365k4j7t5gFC1R1/0X99OQ==
Source149:      https://registry.npmjs.org/@girs/st-18/-/st-18-4.9.0.tgz
%define         SHA512SUM149 VMdgmklmH2wDc0CgASmUQDtruTmQCdIqWm8/5F6Ks5URDkP3FRucrq88avXlaerWRN/dwikYT0UQfJPT+Dw8IQ==
Source150:      https://registry.npmjs.org/@girs/upowerglib-1.0/-/upowerglib-1.0-4.9.0.tgz
%define         SHA512SUM150 wGptYb4WqkVElyi55ThMcfEumwgx5io6dN1aGzKYyxtyamrPLCKHwt3NGRXYXDR9fKkTTpEA6IdYvLF7717lqQ==
Source151:      https://registry.npmjs.org/@girs/xfixes-4.0/-/xfixes-4.0-4.9.0.tgz
%define         SHA512SUM151 vyCuTgWrgHAGSP3DYrNgP73nQ5AsyGvjjLLapjU06jUJkixxCd0wceXrkFnVJQsXjUT3nfU9yXgdy2vZsJnBVA==
Source152:      https://registry.npmjs.org/@girs/xlib-2.0/-/xlib-2.0-4.9.0.tgz
%define         SHA512SUM152 jOMEq91LT410DiJwDo7Xq5yLp5Al0seYZy+rF2YpGUvyfCxOgkmLPTWvhSc4IEJ4AMv+C4d/2suvGh3OUiTHJg==
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
Source158:      https://registry.npmjs.org/@keyv/bigmap/-/bigmap-1.3.1.tgz
%define         SHA512SUM158 WbzE9sdmQtKy8vrNPa9BRnwZh5UF4s1KTmSK0KUVLo3eff5BlQNNWDnFOouNpKfPKDnms9xynJjsMYjMaT/aFQ==
Source159:      https://registry.npmjs.org/@keyv/serialize/-/serialize-1.1.1.tgz
%define         SHA512SUM159 dXn3FZhPv0US+7dtJsIi2R+c7qWYiReoEh5zUntWCf4oSpMNib8FDhSoed6m3QyZdx5hK7iLFkYk3rNxwt8vTA==
Source160:      https://registry.npmjs.org/@parcel/watcher/-/watcher-2.6.0.tgz
%define         SHA512SUM160 7FNeNl8NCE7aINx7WXiKQrPYZWC/hvrTsmk6zmxbI7LTXE7hVek/n8AfVgpe2y82zl3w0HvCHN0bVKMBoJcC0w==
Source161:      https://registry.npmjs.org/@parcel/watcher-linux-arm-glibc/-/watcher-linux-arm-glibc-2.6.0.tgz
%define         SHA512SUM161 Ps/hui3A+vMbjdqlqAowK2ZL8+BO8dBjxeWXj6npTBs3jx4wWmbPpaLuqwrQrSqIVMCnpWo238bJ1U37GhQOYg==
Source162:      https://registry.npmjs.org/@parcel/watcher-linux-arm-musl/-/watcher-linux-arm-musl-2.6.0.tgz
%define         SHA512SUM162 9c6AUHgHoG+IY88MRIHupztQiQnrbqHYQjkM2btA+Bf/wQnQMuiD0Wfk1EVv3TlNT3x41uU71rn6E4xh/+zvkw==
Source163:      https://registry.npmjs.org/@parcel/watcher-linux-arm64-glibc/-/watcher-linux-arm64-glibc-2.6.0.tgz
%define         SHA512SUM163 yHRqS2owEXe6Hic9z6Mh1ECsCd+ODVOGvZDyciqRd21+v+o+DnXMOrw50DSpIG2sb8GPEaPPmfeCAWKPJdq46g==
Source164:      https://registry.npmjs.org/@parcel/watcher-linux-arm64-musl/-/watcher-linux-arm64-musl-2.6.0.tgz
%define         SHA512SUM164 WhB2e/V7rqdHHWZusBSPuy5Ei8S6lSz6FE5TKKQz5h3a0O+C+mhY7vxU9b/stqvMb8beLnPY82ZrFTLKs+SrKA==
Source165:      https://registry.npmjs.org/@parcel/watcher-linux-x64-glibc/-/watcher-linux-x64-glibc-2.6.0.tgz
%define         SHA512SUM165 ulGE6x6Oz6iAwg75T8YQSoguBWasniIbX+QWpaYPcCnDOpdWX3k+4xbEYPZVLxOuoJI+svJJPD3sEj8G7lrQ3A==
Source166:      https://registry.npmjs.org/@parcel/watcher-linux-x64-musl/-/watcher-linux-x64-musl-2.6.0.tgz
%define         SHA512SUM166 tkBYKt7YQrjIJWYDnto2YgO8MRkjlMTSNoRHzsXinBqbLdeOM3L32wPZJvIZxqaLMfSlS/4sUjH/6STVP/XDLw==
Source167:      https://registry.npmjs.org/@stylistic/eslint-plugin/-/eslint-plugin-5.10.0.tgz
%define         SHA512SUM167 nPK52ZHvot8Ju/0A4ucSX1dcPV2/1clx0kLcH5wDmrE4naKso7TUC/voUyU1O9OTKTrR6MYip6LP0ogEMQ9jPQ==
Source168:      https://registry.npmjs.org/@types/esrecurse/-/esrecurse-4.3.1.tgz
%define         SHA512SUM168 xJBAbDifo5hpffDBuHl0Y8ywswbiAp/Wi7Y/GtAgSlZyIABppyurxVueOPE8LUQOxdlgi6Zqce7uoEpqNTeiUw==
Source169:      https://registry.npmjs.org/@types/estree/-/estree-1.0.9.tgz
%define         SHA512SUM169 GhdPgy1el4/ImP05X05Uw4cw2/M93BCUmnEvWZNStlCzEKME4Fkk+YpoA5OiHNQmoS7Cafb8Xa3Pya8m1Qrzeg==
Source170:      https://registry.npmjs.org/@types/json-schema/-/json-schema-7.0.15.tgz
%define         SHA512SUM170 5+fP8P8MFNC+AyZCDxrB2pkZFPGzqQWUzpSeuuVLvm8VMcorNYavBqoFcxK8bQz4Qsbn4oUEEem4wDLfcysGHA==
Source171:      https://registry.npmjs.org/@typescript-eslint/eslint-plugin/-/eslint-plugin-8.70.0.tgz
%define         SHA512SUM171 /v8HZt6RlyIZxB3ntehELOcUcfxKPVGWXnQdJuHRmzrqgF8nQypcC/oxGW+Ot4VGKDq81XugPKxx0n5PBtf9PA==
Source172:      https://registry.npmjs.org/ignore/-/ignore-7.0.9.tgz
%define         SHA512SUM172 brTTsvFRt5C1gGHtPst/281UjPD5t9fBqbgoMPlVWy11ZLTPfu7HxK4ZYqO9H7o/yC9rSTCI85EaQ4OoY12qYw==
Source173:      https://registry.npmjs.org/@typescript-eslint/parser/-/parser-8.70.0.tgz
%define         SHA512SUM173 zYvrmj9Yxd63UGaXw+kdt6A0F0s0qveJyuatIM77bYC2DE4pgmg7a50u8LR7PRtXd0x+h+Tl3eXabGm06SWd3Q==
Source174:      https://registry.npmjs.org/@typescript-eslint/project-service/-/project-service-8.70.0.tgz
%define         SHA512SUM174 hFHbTNqhU9G+2eKFXCBVb1tjFT/LceiJ4+HfLO4pTpDI0KHi6iajpcFFkaSQ9gXmCh7n82A0PthaayEdN6mspQ==
Source175:      https://registry.npmjs.org/@typescript-eslint/scope-manager/-/scope-manager-8.70.0.tgz
%define         SHA512SUM175 8nP3Kwh5hlgZ4FicGvmznAmJe8UL4sdU8tLukrPaMuQmDuk4Y8xYfzu/aYZW4xT2JCgc7H/TpDI5cGlxcWJSqQ==
Source176:      https://registry.npmjs.org/@typescript-eslint/tsconfig-utils/-/tsconfig-utils-8.70.0.tgz
%define         SHA512SUM176 adnkeeNq9Sq1sUf4+FRVc0KdgYghzsgFpZSQVZVvY0LCuUuN0FnQgyGzCJeC4fW1cdXseBAjU2EOqUIjbNcZUw==
Source177:      https://registry.npmjs.org/@typescript-eslint/type-utils/-/type-utils-8.70.0.tgz
%define         SHA512SUM177 NUMKIhYVaVIVLnRL9CRt+VVcuLgSHUCpXn4/+K8wql+vdInUzvx8BjUO1oJ7cG9shjFJKtF8F8Hh2kCh3/KBVw==
Source178:      https://registry.npmjs.org/@typescript-eslint/types/-/types-8.70.0.tgz
%define         SHA512SUM178 asTOIYhDg4zdzOScCyaytrsV3cR6B4ecPQlXw/dJIm7J/MZTtCtfVII9JD8Geh4jTCrK/Xe6cg5UevoleMcoJQ==
Source179:      https://registry.npmjs.org/@typescript-eslint/typescript-estree/-/typescript-estree-8.70.0.tgz
%define         SHA512SUM179 d9NmHMPEKQ7QCLLm1jI3zmoQBwT5KwFYjXBJ9ymZfKCUU+5rmTRykKAFvH5Qn/ZCds3CEAFS9OC9M/jkl0X2bA==
Source180:      https://registry.npmjs.org/@typescript-eslint/utils/-/utils-8.70.0.tgz
%define         SHA512SUM180 oZmtKJz/4fufZ2p3+Cn3ijEojcdfR+1zYDH2xKYrEly0dR/Q/1xUPRCOlKGxod78nWlU2UnDe09GZ3TaknBFGA==
Source181:      https://registry.npmjs.org/@typescript-eslint/visitor-keys/-/visitor-keys-8.70.0.tgz
%define         SHA512SUM181 BoC8PiO4Hkdo0TVJh9Ntxr5MxPDI7/oFsrygN5ADelFSeXG/qgNuucIGA+L5Z6JpPTE/uRfcTWtscjbUaufepQ==
Source182:      https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-5.0.1.tgz
%define         SHA512SUM182 tD40eHxA35h0PEIZNeIjkHoDR4YjjJp34biM0mDvplBe//mB+IHCqHDGV7pxF+7MklTvighcCPPZC7ynWyjdTA==
Source183:      https://registry.npmjs.org/typescript/-/typescript-7.0.2.tgz
%define         SHA512SUM183 8FYau96o3NKOhbjKi/qNvG/W5jhzxkbdm5sj9AbZ/5T5sWqn3hJgLfGx27sRKZWTvyzCP8dLRBTf5tBTSRVUNA==
Source184:      https://registry.npmjs.org/typescript/-/typescript-6.0.3.tgz
%define         SHA512SUM184 y2TvuxSZPDyQakkFRPZHKFm+KKVqIisdg9/CZwm9ftvKXLP8NRWj38/ODjNbr43SsoXqNuAisEf1GdCxqWcdBw==
Source185:      https://registry.npmjs.org/@typescript/typescript-linux-arm/-/typescript-linux-arm-7.0.2.tgz
%define         SHA512SUM185 gffT3xPz9sR7j/YJExkyPntrI0P2EP9XbOyWzth2/Gs0RstK+90RBcO0ncXoXy/beYll1SXw846Nf2zdnEz0QQ==
Source186:      https://registry.npmjs.org/@typescript/typescript-linux-arm64/-/typescript-linux-arm64-7.0.2.tgz
%define         SHA512SUM186 Qh4eU4/y3yDjnfjjyPYihMj5/ODIlmt+Bzu17OI+fiSRDW57QmU5SiN63exPRNJPKUzcc1INa1NXdrJ+MqHjUQ==
Source187:      https://registry.npmjs.org/@typescript/typescript-linux-loong64/-/typescript-linux-loong64-7.0.2.tgz
%define         SHA512SUM187 uEHck9i8hoAzXPiYRib1O7miOnz23SxIeVl6F4LXox+qov1K35jHcEW6VHKvZI+pyvl7fZEP4MCU5LYvIq1GuQ==
Source188:      https://registry.npmjs.org/@typescript/typescript-linux-mips64el/-/typescript-linux-mips64el-7.0.2.tgz
%define         SHA512SUM188 R4KvAMnE43W5Qeqb0Ly56O3mWMWIAgsMyz36DCaycd5nbg/9kzm0liw3JocfRqyJY0KPmzFjbswozXyW0DnIYA==
Source189:      https://registry.npmjs.org/@typescript/typescript-linux-ppc64/-/typescript-linux-ppc64-7.0.2.tgz
%define         SHA512SUM189 DORx5b3sd/4S7eayxm4FQv+A7CrkUIGRaHiwI8oiHTAI1fAPWhF4J0vAlkC8biAlHSVVwxMQ3tjZ2/DVbnQiiA==
Source190:      https://registry.npmjs.org/@typescript/typescript-linux-riscv64/-/typescript-linux-riscv64-7.0.2.tgz
%define         SHA512SUM190 wf0jqEDOjrPRnKwYRyyJDRo11KMbvMFrU+q4zqKyChODBzvlkbhNQfKvLxQCcwTpdDaXSHZTVuh0JoCrKCUMHQ==
Source191:      https://registry.npmjs.org/@typescript/typescript-linux-s390x/-/typescript-linux-s390x-7.0.2.tgz
%define         SHA512SUM191 IkwJc3L7yhytWd/ewjyxNDfOmswCm9GWMJT/ue/dU4aZNbwZeYAetq42VyLmsmSjvoX7z74X6ZaYCtzAr0EuGw==
Source192:      https://registry.npmjs.org/@typescript/typescript-linux-x64/-/typescript-linux-x64-7.0.2.tgz
%define         SHA512SUM192 EYdf2cNg7rgCWJnxCdJ+F3V39O8ihb37eHAu1LK8oAFizgTQbPOK7zHHXbPt8rX24COqODXeI3sIf0fCXG7H/A==
Source193:      https://registry.npmjs.org/acorn/-/acorn-8.18.0.tgz
%define         SHA512SUM193 lGq+9yr1/GuAWaVYIHRjvvySG5/4VfKIvC8EWxStPdcDh/Ka7FG3twP6v4d5BkravUilhIAsG4Qj83t02LWUPQ==
Source194:      https://registry.npmjs.org/acorn-jsx/-/acorn-jsx-5.3.2.tgz
%define         SHA512SUM194 rq9s+JNhf0IChjtDXxllJ7g41oZk5SlXtp0LHwyA5cejwn7vKmKp4pPri6YEePv2PU65sAsegbXtIinmDFDXgQ==
Source195:      https://registry.npmjs.org/ajv/-/ajv-6.15.0.tgz
%define         SHA512SUM195 fgFx7Hfoq60ytK2c7DhnF8jIvzYgOMxfugjLOSMHjLIPgenqa7S7oaagATUq99mV6IYvN2tRmC0wnTYX6iPbMw==
Source196:      https://registry.npmjs.org/balanced-match/-/balanced-match-4.0.4.tgz
%define         SHA512SUM196 BLrgEcRTwX2o6gGxGOCNyMvGSp35YofuYzw9h1IMTRmKqttAZZVU67bdb9Pr2vUHA8+j3i2tJfjO6C6+4myGTA==
Source197:      https://registry.npmjs.org/brace-expansion/-/brace-expansion-5.0.9.tgz
%define         SHA512SUM197 ScQ4IuvIEF1TMlP7Zt+vjJ//9zlPb2SDcxWxM3bk8s6t6GGdJ7KO1dCcTidOPJKePW30LE/2cT7wCyPho9/Wxg==
Source198:      https://registry.npmjs.org/cacheable/-/cacheable-2.5.0.tgz
%define         SHA512SUM198 60cyAOytib/OzBw1JNSoSV/boK1AtHryDIjvVBk7XbN4ugfkM3+Sry7fEjNgPMGgOjuaZPAp8ruZ0Cxafwyq9g==
Source199:      https://registry.npmjs.org/chokidar/-/chokidar-5.0.0.tgz
%define         SHA512SUM199 TQMmc3w+5AxjpL8iIiwebF73dRDF4fBIieAqGn9RGCWaEVwQ6Fb2cGe31Yns0RRIzii5goJ1Y7xbMwo1TxMplw==
Source200:      https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.6.tgz
%define         SHA512SUM200 uV2QOWP2nWzsy2aMp8aRibhi9dlzF5Hgh5SHaB9OiTGEyDTiJJyx0uy51QXdyWbtAHNua4XJzUKca3OzKUd3vA==
Source201:      https://registry.npmjs.org/debug/-/debug-4.4.3.tgz
%define         SHA512SUM201 RGwwWnwQvkVfavKVt22FGLw+xYSdzARwm0ru6DhTVA3umU5hZc28V3kO4stgYryrTlLpuvgI9GiijltAjNbcqA==
Source202:      https://registry.npmjs.org/deep-is/-/deep-is-0.1.4.tgz
%define         SHA512SUM202 oIPzksmTg4/MriiaYGO+okXDT7ztn/w3Eptv/+gSIdMdKsJo0u4CfYNFJPy+4SKMuCqGw2wxnA+URMg3t8a/bQ==
Source203:      https://registry.npmjs.org/detect-libc/-/detect-libc-2.1.2.tgz
%define         SHA512SUM203 Btj2BOOO83o3WyH59e8MgXsxEQVcarkUOpEYrubB0urwnN10yQ364rsiByU11nZlqWYZm05i/of7io4mzihBtQ==
Source204:      https://registry.npmjs.org/escape-string-regexp/-/escape-string-regexp-4.0.0.tgz
%define         SHA512SUM204 TtpcNJ3XAzx3Gq8sWRzJaVajRs0uVxA2YAkdb1jm2YkPz4G6egUFAyA3n5vtEIZefPk5Wa4UXbKuS5fKkJWdgA==
Source205:      https://registry.npmjs.org/eslint/-/eslint-10.10.0.tgz
%define         SHA512SUM205 NPXn6r5zl4uET1DAVPaOwzX3rut4c0wcmw3dWJAfOsTM5+TogXo0DDjz8pwm/hL8cyVNpHqeK4JpN0NjnyFFNw==
Source206:      https://registry.npmjs.org/eslint-scope/-/eslint-scope-9.1.2.tgz
%define         SHA512SUM206 xS90H51cKw0jltxmvmHy2Iai1LIqrfbw57b79w/J7MfvDfkIkFZ+kj6zC3BjtUwh150HsSSdxXZcsuv72miDFQ==
Source207:      https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-4.2.1.tgz
%define         SHA512SUM207 Uhdk5sfqcee/9H/rCOJikYz67o0a2Tw2hGRPOG2Y1R2dg7brRe1uG0yaNQDHu+TO/uQPF/5eCapvYSmHUjt7JQ==
Source208:      https://registry.npmjs.org/eslint-visitor-keys/-/eslint-visitor-keys-5.0.1.tgz
%define         SHA512SUM208 tD40eHxA35h0PEIZNeIjkHoDR4YjjJp34biM0mDvplBe//mB+IHCqHDGV7pxF+7MklTvighcCPPZC7ynWyjdTA==
Source209:      https://registry.npmjs.org/espree/-/espree-11.2.0.tgz
%define         SHA512SUM209 7p3DrVEIopW1B1avAGLuCSh1jubc01H2JHc8B4qqGblmg5gI9yumBgACjWo4JlIc04ufug4xJ3SQI8HkS/Rgzw==
Source210:      https://registry.npmjs.org/espree/-/espree-10.4.0.tgz
%define         SHA512SUM210 j6PAQ2uUr79PZhBjP5C5fhl8e39FmRnOjsD5lGnWrFU8i2G776tBK7+nP8KuQUTTyAZUwfQqXAgrVH5MbH9CYQ==
Source211:      https://registry.npmjs.org/esquery/-/esquery-1.7.0.tgz
%define         SHA512SUM211 Ap6G0WQwcU/LHsvLwON1fAQX9Zp0A2Y6Y/cJBl9r/JbW90Zyg4/zbG6zzKa2OTALELarYHmKu0GhpM5EO+7T0g==
Source212:      https://registry.npmjs.org/esrecurse/-/esrecurse-4.3.0.tgz
%define         SHA512SUM212 KmfKL3b6G+RXvP8N1vr3Tq1kL/oCFgn2NYXEtqP8/L3pKapUA4G8cFVaoF3SU323CD4XypR/ffioHmkti6/Tag==
Source213:      https://registry.npmjs.org/estraverse/-/estraverse-5.3.0.tgz
%define         SHA512SUM213 MMdARuVEQziNTeJD8DgMqmhwR11BRQ/cBP+pLtYdSTnf3MIO8fFeiINEbX36ZdNlfU/7A9f3gUw49B3oQsvwBA==
Source214:      https://registry.npmjs.org/esutils/-/esutils-2.0.3.tgz
%define         SHA512SUM214 kVscqXk4OCp68SZ0dkgEKVi6/8ij300KBWTJq32P/dYeWTSwK41WyTxalN1eRmA5Z9UU/LX9D7FWSmV9SAYx6g==
Source215:      https://registry.npmjs.org/fast-deep-equal/-/fast-deep-equal-3.1.3.tgz
%define         SHA512SUM215 f3qQ9oQy9j2AhBe/H9VC91wLmKBCCU/gDOnKNAYG5hswO7BLKj09Hc5HYNz9cGI++xlpDCIgDaitVs03ATR84Q==
Source216:      https://registry.npmjs.org/fast-json-stable-stringify/-/fast-json-stable-stringify-2.1.0.tgz
%define         SHA512SUM216 lhd/wF+Lk98HZoTCtlVraHtfh5XYijIjalXck7saUtuanSDyLMxnHhSXEDJqHxD7msR8D0uCmqlkwjCV8xvwHw==
Source217:      https://registry.npmjs.org/fast-levenshtein/-/fast-levenshtein-2.0.6.tgz
%define         SHA512SUM217 DCXu6Ifhqcks7TZKY3Hxp3y6qphY5SJZmrWMDrKcERSOXWQdMhU9Ig/PYrzyw/ul9jOIyh0N4M0tbC5hodg8dw==
Source218:      https://registry.npmjs.org/fdir/-/fdir-6.5.0.tgz
%define         SHA512SUM218 tIbYtZbucOs0BRGqPJkshJUYdL+SDH7dVM8gjy+ERp3WAUjLEFJE+02kanyHtwjWOnwrKYBiwAmM0p4kLJAnXg==
Source219:      https://registry.npmjs.org/file-entry-cache/-/file-entry-cache-11.1.5.tgz
%define         SHA512SUM219 +PFTHITI08JIGhnNpGNI8T8inUpgZfk3GNEqfT9R2zZV2iFXg3CvqzSl/uEhs7TSGujYRELEANyDvS8Fj7+S7Q==
Source220:      https://registry.npmjs.org/find-up/-/find-up-5.0.0.tgz
%define         SHA512SUM220 78/PXT1wlLLDgTzDs7sjq9hzz0vXD+zn+7wypEe4fXQxCmdmqfGsEPQxmiCSQI3ajFV91bVSsvNtrJRiW6nGng==
Source221:      https://registry.npmjs.org/flat-cache/-/flat-cache-6.1.23.tgz
%define         SHA512SUM221 f++BY9pTk+983xK1FLzlLpmM0i0z+jHmx3QESGkURMXujQZz1k5wzwX6hjnQ8goaD0B+sYnDK1yZ6MTyZfUaqA==
Source222:      https://registry.npmjs.org/flatted/-/flatted-3.4.4.tgz
%define         SHA512SUM222 5+ybhBZANEJxaH3X5evAFatUxLfEHSr7n6kYJ+1Qd0mUqr4eu9gIf6GDbWHf8RJijHrjjO8G+la14SlL2SeS1Q==
Source223:      https://registry.npmjs.org/glob-parent/-/glob-parent-6.0.2.tgz
%define         SHA512SUM223 XxwI8EOhVQgWp6iDL+3b0r86f4d6AX6zSU55HfB4ydCEuXLXc5FcYeOu+nnGftS4TEju/11rt4KJPTMgbfmv4A==
Source224:      https://registry.npmjs.org/hashery/-/hashery-1.5.1.tgz
%define         SHA512SUM224 iZyKG96/JwPz1N55vj2Ie2vXbhu440zfUfJvSwEqEbeLluk7NnapfGqa7LH0mOsnDxTF85Mx8/dyR6HfqcbmbQ==
Source225:      https://registry.npmjs.org/hookified/-/hookified-1.15.1.tgz
%define         SHA512SUM225 MvG/clsADq1GPM2KGo2nyfaWVyn9naPiXrqIe4jYjXNZQt238kWyOGrsyc/DmRAQ+Re6yeo6yX/yoNCG5KAEVg==
Source226:      https://registry.npmjs.org/ignore/-/ignore-5.3.2.tgz
%define         SHA512SUM226 hsBTNUqQTDwkWtcdYI2i06Y/nUBEsNEDJKjWdigLvegy8kDuJAS8uRlpkkcQpyEXL0Z/pjDy5HBmMjRCJ2gq+g==
Source227:      https://registry.npmjs.org/immutable/-/immutable-5.1.9.tgz
%define         SHA512SUM227 m8nVez3rwrgmWxtLMt1ZYXB2Lv7OKYn/disyxAlSDYAlKSlFoPPfIAmAM/M5xqL4m4C/wAPw7S2/CNaUii1Hxg==
Source228:      https://registry.npmjs.org/imurmurhash/-/imurmurhash-0.1.4.tgz
%define         SHA512SUM228 JmXMZ6wuvDmLiHEml9ykzqO6lwFbof0GG4IkcGaENdCRDDmMVnny7s5HsIgHCbaq0w2MyPhDqkhTUgS2LU2PHA==
Source229:      https://registry.npmjs.org/is-extglob/-/is-extglob-2.1.1.tgz
%define         SHA512SUM229 SbKbANkN603Vi4jEZv49LeVJMn4yGwsbzZworEoyEiutsN3nJYdbO36zfhGJ6QEDpOZIFkDtnq5JRxmvl3jsoQ==
Source230:      https://registry.npmjs.org/is-glob/-/is-glob-4.0.3.tgz
%define         SHA512SUM230 xelSayHH36ZgE7ZWhli7pW34hNbNl8Ojv5KVmkJD4hBdD3th8Tfk9vYasLM+mXWOZhFkgZfxhLSnrwRr4elSSg==
Source231:      https://registry.npmjs.org/isexe/-/isexe-2.0.0.tgz
%define         SHA512SUM231 RHxMLp9lnKHGHRng9QFhRCMbYAcVpn69smSGcq3f36xjgVVWThj4qqLbTLlq7Ssj8B+fIQ1EuCEGI2lKsyQeIw==
Source232:      https://registry.npmjs.org/json-schema-traverse/-/json-schema-traverse-0.4.1.tgz
%define         SHA512SUM232 xbbCH5dCYU5T8LcEhhuh7HJ88HXuW3qsI3Y0zOZFKfZEHcpWiHU/Jxzk629Brsab/mMiHQti9wMP+845RPe3Vg==
Source233:      https://registry.npmjs.org/json-stable-stringify-without-jsonify/-/json-stable-stringify-without-jsonify-1.0.1.tgz
%define         SHA512SUM233 Bdboy+l7tA3OGW6FjyFHWkP5LuByj1Tk33Ljyq0axyzdk9//JSi2u3fP1QSmd1KNwq6VOKYGlAu87CisVir6Pw==
Source234:      https://registry.npmjs.org/keyv/-/keyv-5.6.0.tgz
%define         SHA512SUM234 CYDD3SOtsHtyXeEORYRx2qBtpDJFjRTGXUtmNEMGyzYOKj1TE3tycdlho7kA1Ufx9OYWZzg52QFBGALTirzDSw==
Source235:      https://registry.npmjs.org/levn/-/levn-0.4.1.tgz
%define         SHA512SUM235 +bT2uH4E5LGE7h/n3evcS/sQlJXCpIp6ym8OWJ5eV6+67Dsql/LaaT7qJBAt2rzfoa/5QBGBhxDix1dMt2kQKQ==
Source236:      https://registry.npmjs.org/locate-path/-/locate-path-6.0.0.tgz
%define         SHA512SUM236 iPZK6eYjbxRu3uB4/WZ3EsEIMJFMqAoopl3R+zuq0UjcAm/MO6KCweDgPfP3elTztoKP3KtnVHxTn2NHBSDVUw==
Source237:      https://registry.npmjs.org/minimatch/-/minimatch-10.2.6.tgz
%define         SHA512SUM237 vpLQEs+VLCr1nU0BXS07maYoFwlDAH0gngQuuttxIwutDFEMHq2blX+8vpgxDdK3J1PwjCJiep77OitTZ4Ll1A==
Source238:      https://registry.npmjs.org/ms/-/ms-2.1.3.tgz
%define         SHA512SUM238 6FlzubTLZG3J2a/NVCAleEhjzq5oxgHyaCU9yYXvcLsvoVaHJq/s5xXI6/XXP6tz7R9xAOtHnSO/tXtF3WRTlA==
Source239:      https://registry.npmjs.org/natural-compare/-/natural-compare-1.4.0.tgz
%define         SHA512SUM239 OWND8ei3VtNC9h7V60qff3SVobHr996CTwgxubgyQYEpg290h9J0buyECNNJexkFm5sOajh5G116RYA1c8ZMSw==
Source240:      https://registry.npmjs.org/node-addon-api/-/node-addon-api-7.1.1.tgz
%define         SHA512SUM240 5m3bsyrjFWE1xf7nz7YXdN4udnVtXK6/Yfgn5qnahL6bCkf2yKt4k3nuTKAtT4r3IG8JNR2ncsIMdZuAzJjHQQ==
Source241:      https://registry.npmjs.org/optionator/-/optionator-0.9.4.tgz
%define         SHA512SUM241 6IpQ7mKUxRcZNLIObR0hz7lxsapSSIYNZJwXPGeF0mTVqGKFIXj1DQcMoT22S3ROcLyY/rz0PWaWZ9ayWmad9g==
Source242:      https://registry.npmjs.org/p-limit/-/p-limit-3.1.0.tgz
%define         SHA512SUM242 TYOanM3wGwNGsZN2cVTYPArw454xnXj5qmWF1bEoAc4+cU/ol7GVh7odevjp1FNHduHc3KZMcFduxU5Xc6uJRQ==
Source243:      https://registry.npmjs.org/p-locate/-/p-locate-5.0.0.tgz
%define         SHA512SUM243 LaNjtRWUBY++zB5nE/NwcaoMylSPk+S+ZHNB1TzdbMJMny6dynpAGt7X/tl/QYq3TIeE6nxHppbo2LGymrG5Pw==
Source244:      https://registry.npmjs.org/path-exists/-/path-exists-4.0.0.tgz
%define         SHA512SUM244 ak9Qy5Q7jYb2Wwcey5Fpvg2KoAc/ZIhLSLOSBmRmygPsGwkVVt0fZa0qrtMz+m6tJTAHfZQ8FnmB4MG4LWy7/w==
Source245:      https://registry.npmjs.org/path-key/-/path-key-3.1.1.tgz
%define         SHA512SUM245 ojmeN0qd+y0jszEtoY48r0Peq5dwMEkIlCOu6Q5f41lfkswXuKtYrhgoTpLnyIcHm24Uhqx+5Tqm2InSwLhE6Q==
Source246:      https://registry.npmjs.org/picomatch/-/picomatch-4.0.7.tgz
%define         SHA512SUM246 qcJu88Q2IWqJsDD529JKMdwGm/dvInW4HvQnRwiH9JtihJvzGOscDtHE3x1pBKeUOTysQ8kVmLnJ2kJu7yhcGA==
Source247:      https://registry.npmjs.org/prelude-ls/-/prelude-ls-1.2.1.tgz
%define         SHA512SUM247 vkcDPrRZo1QZLbn5RLGPpg/WmIQ65qoWWhcGKf/b5eplkkarX0m9z8ppCat4mlOqUsWpyNuYgO3VRyrYHSzX5g==
Source248:      https://registry.npmjs.org/punycode/-/punycode-2.3.1.tgz
%define         SHA512SUM248 vYt7UD1U9Wg6138shLtLOvdAu+8DsC/ilFtEVHcH+wydcSpNE20AfSOduf6MkRFahL5FY7X1oU7nKVZFtfq8Fg==
Source249:      https://registry.npmjs.org/qified/-/qified-0.10.1.tgz
%define         SHA512SUM249 +Owyggi9IxT1ePKGafcI87ubSmxol6smwJ+RAHDQlx9+9cPwFWDiKFFCPuWhr9ignlGpZ9vDQLw67N4dcTVFEA==
Source250:      https://registry.npmjs.org/hookified/-/hookified-2.2.0.tgz
%define         SHA512SUM250 p/LgFzRN5FeoD3DLS6bkUapeye6E4SI6yJs6KetENd18S+FBthqYq2amJUWpt5z0EQwwHemidjY5OqJGEKm5uA==
Source251:      https://registry.npmjs.org/readdirp/-/readdirp-5.1.1.tgz
%define         SHA512SUM251 Kko+Y5XQ6fM+Ce3dq3m9YGxnacYZYl9cA1wZjaF3Vbry2L3i1qVg8+CAgNPsXRArPMUMCaOR7oa9Nqntc43JKA==
Source252:      https://registry.npmjs.org/sass/-/sass-1.104.0.tgz
%define         SHA512SUM252 btHMApW2bgolvClhRW8AlQJzgI9lUB3pPSofBQQT+E46GWvf9o0TVQ13SYv5riWZVFyPN+JNz3TKW9XhBlc10w==
Source253:      https://registry.npmjs.org/semver/-/semver-7.8.5.tgz
%define         SHA512SUM253 Y7/KDsb8LjooZpwaqGyulO6DQlksgCncchHGk+sZIY4SBvUocMBEFH5Ur1fI4dV+Jvl0w6cjvucaIi40puRioA==
Source254:      https://registry.npmjs.org/shebang-command/-/shebang-command-2.0.0.tgz
%define         SHA512SUM254 kHxr2zZpYtdmrN1qDjrrX/Z1rR1kG8Dx+gkpK1G4eXmvXswmcE1hTWBWYUzlraYw1/yZp6YuDY77YtvbN0dmDA==
Source255:      https://registry.npmjs.org/shebang-regex/-/shebang-regex-3.0.0.tgz
%define         SHA512SUM255 7++dFhtcx3353uBaq8DDR4NuxBetBzC7ZQOhmTQInHEd6bSrXdiEyzCvG07Z44UYdLShWUyXt5M/yhz8ekcb1A==
Source256:      https://registry.npmjs.org/source-map-js/-/source-map-js-1.2.1.tgz
%define         SHA512SUM256 UXWMKhLOwVKb728IUtQPXxfYU+usdybtUrK/8uGE8CQMvrhOpwvzDBwj0QhSL7MQc7vIsISBG8VQ8+IDQxpfQA==
Source257:      https://registry.npmjs.org/tinyglobby/-/tinyglobby-0.2.17.tgz
%define         SHA512SUM257 wXR/dYpcqKmfWpEdZjiKJOwCNFndD0DMnrW/cYjVGttEkBfVgcLFHoNrlj47mjOVic9yyNu65alsgF4NQyTa2g==
Source258:      https://registry.npmjs.org/ts-api-utils/-/ts-api-utils-2.5.0.tgz
%define         SHA512SUM258 OJ/ibxhPlqrMM0UiNHJ/0CKQkoKF243/AEmplt3qpRgkW8VG7IfOS41h7V8TjITqdByHzrjcS/2si+y4lIh8NA==
Source259:      https://registry.npmjs.org/type-check/-/type-check-0.4.0.tgz
%define         SHA512SUM259 XleUoc9uwGXqjWwXaUTZAmzMcFZ5858QA2vvx1Ur5xIcixXIP+8LnFDgRplU30us6teqdlskFfu+ae4K79Ooew==
Source260:      https://registry.npmjs.org/@typescript/typescript6/-/typescript6-6.0.2.tgz
%define         SHA512SUM260 mbCddXd+jm7hfx7w2YU64/Av4/NqqeG3GoRZgxPcgoTxYjhrcfJRw9ULch71SS4G+Q3bOXFhRvPqjguN0Hyp5w==
Source261:      https://registry.npmjs.org/typescript-eslint/-/typescript-eslint-8.70.0.tgz
%define         SHA512SUM261 P/W5cz70/cQAuKfY3xwQMWWTV7BvJ0mAQmi+9mBcsVPaBUpd6Ohpa+fECv9rBFrQcig86jAiNBFNWUqnTjr4pw==
Source262:      https://registry.npmjs.org/uri-js/-/uri-js-4.4.1.tgz
%define         SHA512SUM262 7rKUyy33Q1yc98pQ1DAmLtwX109F7TIfWlW1Ydo8Wl1ii1SeHieeh0HHfPeL2fMXK6z0s8ecKs9frCuLJvndBg==
Source263:      https://registry.npmjs.org/which/-/which-2.0.2.tgz
%define         SHA512SUM263 BLI3Tl1TW3Pvl70l3yq3Y64i+awpwXqsGBYWkkqMtnbXgrMD+yj7rhW0kuEDxzJaYXGjEW5ogapKNMEKNMjibA==
Source264:      https://registry.npmjs.org/word-wrap/-/word-wrap-1.2.5.tgz
%define         SHA512SUM264 BN22B5eaMMI9UMtjrGd5g5eCYPpCPDUy0FJXbYsaT5zYxjFOckS53SQDE3pWkVoWpHXVb3BrYcEN4Twa55B5cA==
Source265:      https://registry.npmjs.org/yocto-queue/-/yocto-queue-0.1.0.tgz
%define         SHA512SUM265 rVksvsnNCdJ/ohGc6xgPwyN8eheCxsiLM8mxuE/t/mOVqJewPuO1miLpTHQiRgTKCLexL4MeAFVagts7HmNZ2Q==
# END NPM SOURCES

BuildRequires:  nodejs-devel
BuildRequires:  nodejs22-npm
BuildRequires:  make

Requires:       gnome-shell >= 48
Recommends:     gnome-extensions-app
Recommends:     %{name}-shortcut-overrides = %{version}-%{release}
Provides:       %{extension} = %{version}-%{release}
Obsoletes:      gnome-shell-extension-pop-shell < 1.2.1
Obsoletes:      gnome-shell-extension-pop-shell < 1:1.2.1


%description
Shatter Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows.  The core feature of Shatter Shell
is the addition of advanced tiling window management - a feature that has been
highly sought within our community.  For many - ourselves included - i3wm has
become the leading competitor to the GNOME desktop.

Shatter Shell is a fork of Pop Shell.


%package shortcut-overrides
Summary:        Shortcut overrides for %{name}
Obsoletes:      gnome-shell-extension-pop-shell-shortcut-overrides < 1.2.1
Obsoletes:      gnome-shell-extension-pop-shell-shortcut-overrides < 1:1.2.1


%description shortcut-overrides
Shortcut overrides for %{name}.


%prep
%autosetup -p 1 -n %{extension}-%{version}
# START NPM CACHE ADD
npm cache add %{SOURCE100}
npm cache add %{SOURCE101}
npm cache add %{SOURCE102}
npm cache add %{SOURCE103}
npm cache add %{SOURCE104}
npm cache add %{SOURCE105}
npm cache add %{SOURCE106}
npm cache add %{SOURCE107}
npm cache add %{SOURCE108}
npm cache add %{SOURCE109}
npm cache add %{SOURCE110}
npm cache add %{SOURCE111}
npm cache add %{SOURCE112}
npm cache add %{SOURCE113}
npm cache add %{SOURCE114}
npm cache add %{SOURCE115}
npm cache add %{SOURCE116}
npm cache add %{SOURCE117}
npm cache add %{SOURCE118}
npm cache add %{SOURCE119}
npm cache add %{SOURCE120}
npm cache add %{SOURCE121}
npm cache add %{SOURCE122}
npm cache add %{SOURCE123}
npm cache add %{SOURCE124}
npm cache add %{SOURCE125}
npm cache add %{SOURCE126}
npm cache add %{SOURCE127}
npm cache add %{SOURCE128}
npm cache add %{SOURCE129}
npm cache add %{SOURCE130}
npm cache add %{SOURCE131}
npm cache add %{SOURCE132}
npm cache add %{SOURCE133}
npm cache add %{SOURCE134}
npm cache add %{SOURCE135}
npm cache add %{SOURCE136}
npm cache add %{SOURCE137}
npm cache add %{SOURCE138}
npm cache add %{SOURCE139}
npm cache add %{SOURCE140}
npm cache add %{SOURCE141}
npm cache add %{SOURCE142}
npm cache add %{SOURCE143}
npm cache add %{SOURCE144}
npm cache add %{SOURCE145}
npm cache add %{SOURCE146}
npm cache add %{SOURCE147}
npm cache add %{SOURCE148}
npm cache add %{SOURCE149}
npm cache add %{SOURCE150}
npm cache add %{SOURCE151}
npm cache add %{SOURCE152}
npm cache add %{SOURCE153}
npm cache add %{SOURCE154}
npm cache add %{SOURCE155}
npm cache add %{SOURCE156}
npm cache add %{SOURCE157}
npm cache add %{SOURCE158}
npm cache add %{SOURCE159}
npm cache add %{SOURCE160}
npm cache add %{SOURCE161}
npm cache add %{SOURCE162}
npm cache add %{SOURCE163}
npm cache add %{SOURCE164}
npm cache add %{SOURCE165}
npm cache add %{SOURCE166}
npm cache add %{SOURCE167}
npm cache add %{SOURCE168}
npm cache add %{SOURCE169}
npm cache add %{SOURCE170}
npm cache add %{SOURCE171}
npm cache add %{SOURCE172}
npm cache add %{SOURCE173}
npm cache add %{SOURCE174}
npm cache add %{SOURCE175}
npm cache add %{SOURCE176}
npm cache add %{SOURCE177}
npm cache add %{SOURCE178}
npm cache add %{SOURCE179}
npm cache add %{SOURCE180}
npm cache add %{SOURCE181}
npm cache add %{SOURCE182}
npm cache add %{SOURCE183}
npm cache add %{SOURCE184}
npm cache add %{SOURCE185}
npm cache add %{SOURCE186}
npm cache add %{SOURCE187}
npm cache add %{SOURCE188}
npm cache add %{SOURCE189}
npm cache add %{SOURCE190}
npm cache add %{SOURCE191}
npm cache add %{SOURCE192}
npm cache add %{SOURCE193}
npm cache add %{SOURCE194}
npm cache add %{SOURCE195}
npm cache add %{SOURCE196}
npm cache add %{SOURCE197}
npm cache add %{SOURCE198}
npm cache add %{SOURCE199}
npm cache add %{SOURCE200}
npm cache add %{SOURCE201}
npm cache add %{SOURCE202}
npm cache add %{SOURCE203}
npm cache add %{SOURCE204}
npm cache add %{SOURCE205}
npm cache add %{SOURCE206}
npm cache add %{SOURCE207}
npm cache add %{SOURCE208}
npm cache add %{SOURCE209}
npm cache add %{SOURCE210}
npm cache add %{SOURCE211}
npm cache add %{SOURCE212}
npm cache add %{SOURCE213}
npm cache add %{SOURCE214}
npm cache add %{SOURCE215}
npm cache add %{SOURCE216}
npm cache add %{SOURCE217}
npm cache add %{SOURCE218}
npm cache add %{SOURCE219}
npm cache add %{SOURCE220}
npm cache add %{SOURCE221}
npm cache add %{SOURCE222}
npm cache add %{SOURCE223}
npm cache add %{SOURCE224}
npm cache add %{SOURCE225}
npm cache add %{SOURCE226}
npm cache add %{SOURCE227}
npm cache add %{SOURCE228}
npm cache add %{SOURCE229}
npm cache add %{SOURCE230}
npm cache add %{SOURCE231}
npm cache add %{SOURCE232}
npm cache add %{SOURCE233}
npm cache add %{SOURCE234}
npm cache add %{SOURCE235}
npm cache add %{SOURCE236}
npm cache add %{SOURCE237}
npm cache add %{SOURCE238}
npm cache add %{SOURCE239}
npm cache add %{SOURCE240}
npm cache add %{SOURCE241}
npm cache add %{SOURCE242}
npm cache add %{SOURCE243}
npm cache add %{SOURCE244}
npm cache add %{SOURCE245}
npm cache add %{SOURCE246}
npm cache add %{SOURCE247}
npm cache add %{SOURCE248}
npm cache add %{SOURCE249}
npm cache add %{SOURCE250}
npm cache add %{SOURCE251}
npm cache add %{SOURCE252}
npm cache add %{SOURCE253}
npm cache add %{SOURCE254}
npm cache add %{SOURCE255}
npm cache add %{SOURCE256}
npm cache add %{SOURCE257}
npm cache add %{SOURCE258}
npm cache add %{SOURCE259}
npm cache add %{SOURCE260}
npm cache add %{SOURCE261}
npm cache add %{SOURCE262}
npm cache add %{SOURCE263}
npm cache add %{SOURCE264}
npm cache add %{SOURCE265}
# END NPM CACHE ADD


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
* Tue Sep 15 2025 Adil Hanney <adilhanney@disroot.org> - 2.2.1-1
- Fixes:
  - Fixed a stacked window getting stuck as transparent in specific conditions.
  - The Extension Manager app did not display the version of Shatter Shell.
  - Restored stock GNOME's window attention handler. (I can't figure out why this was disabled in pop-shell 5 years ago, but I have no issues on GNOME 51.)
- Smaller fixes:
  - Fixed `entity_eq` not considering the generation of the entities.
  - Fixed an incorrect range check which prevented inserting entities into a storage beyond the current store size.
  - Fixed a bug preventing the 0th storage from being unregistered.
  - Fixed a bug preventing the 0th slot being reused.
- Performance:
  - Only call `reset_visibility` after the new window has been activated (prevents starting an incorrect fade animation which gets immediately cancelled).
- Developer:
  - Replaced rustdoc syntax with jsdoc so that IDE features work.
  - Improved readability by replacing numeric tags with readable strings or self-descriptive booleans.
  - Merged duplicate implementations of Rust-style Result/Ok/Err types.
  - Enabled type-checked eslints and stricter array indexing. This includes minor bug fixes and can prevent similar bugs (listed above) happening in the future.

* Sun Sep 13 2026 Adil Hanney <adilhanney@disroot.org> - 2.2.0-1
- New:
  - Ported the floating exceptions dialog and color chooser dialog to Adwaita/GTK4, and removed all imports of GTK3.
- Developer:
  - Minor cleanups:  this release is 121 lines slimmer

* Sat Sep 12 2026 Adil Hanney <adilhanney@disroot.org> - 2.1.0-1
- New:
  - Added keyboard shortcuts for horizontal workspaces by @laikq in https://github.com/pop-os/shell/pull/1777.
    (Pop!_OS previously only supported vertical workspaces.)
  - Added smarter floating exceptions:
    - Don't tile non-resizeable windows or non-moveable windows, e.g. Steam's sign-in dialog.
    - Don't tile windows with the "skip-taskbar" flag, e.g. XWaylandVideoBridge's invisible window.
    - This nets us wider compatibility and less reliance on an explicit floating exceptions list.
  - Performance improvement in determining which windows to tile by caching compiled RegExp objects.
- Fixed:
  - Ignore no-op stack resize grabs by @philip-sterne in https://github.com/pop-os/shell/pull/1826.
  - Fixed GNOME 48 crash if you click a tab's close button multiple times, based on @siddhpant's fix for https://github.com/pop-os/shell/issues/1794.
  - Replaced pop orange with adwaita blue in another spot that I forgot last release.
- Developer:
  - Suppressed a warning in `make enable` when you don't have the original pop-shell installed.
  - Minor cleanups: this release is 52 lines slimmer

* Fri Sep 11 2026 Adil Hanney <adilhanney@disroot.org> - 2.0.1-1
- New:
  - Improved the smoothness and symmetry of the fade transition between stacked windows.
  - Switched the default active hint color from Pop Orange to Adwaita Blue.
- Fixed:
  - Stack tabs are now clickable even in the 3px gap around each button.
  - Reduced possibility of a window getting stuck as transparent.
- Developer:
  - Formatted code with `@stylistic/eslint-plugin`.
  - Added `checked` attribute to stack tabs, possibly good for accessibility.
  - Improved safety of `window_exec` by passing the `Tab` directly instead of its index.

* Thu Sep 10 2026 Adil Hanney <adilhanney@disroot.org> - 2.0.0-1
- Features:
  - Rebranded from Pop Shell to Shatter Shell.
  - Added GNOME 51 support.
  - Added a setting to stop Shatter Shell from resetting your windows' positions when untiling.
  - Adwaita-themed tab bar for stacked windows: the tabs are bigger and easier to click, and fit in better with GNOME.
  - Added a fade transition when switching between stacked windows.
- Removals:
  - Removed pop-launcher (Super+/) integration in favor of GNOME's overview.
  - Removed system76-scheduler integration, since it's not common outside of Pop!_OS.
  - Removed the "Show Minimize to Tray Windows" setting in favor of stock GNOME Alt+Tab behavior.
  - Removed the "Show Window Titles" setting since it does nothing on Wayland.
- Fixes:
  - Fixed some tiling jank with a fixed `area_right` function.
    This can possibly be upstreamed but needs benchmarking to see if it's actually an improvement or just placebo.
  - Fixed brief flickers in active hints when tiling/untiling/moving windows.
- Floating window exceptions:
  - New: Steam sign-in dialog
  - New: Firefox Picture-in-Picture windows
  - New: Git Credential Manager login popups
  - New: Firefox "About" dialog
  - Fixed: Floating Window Exceptions config window
- Technical:
  - Replaced manual `.d.ts` bindings with `gjsify/gnome-shell`.
  - Updated to Typescript 7 for 10x faster builds and type checking.
  - Enabled eslint for code style and reducing dynamic types.
  - Removed legacy code for X11 and old GNOME versions (47 or older). This is now Wayland only, just like GNOME.
  - Added some basic CI to make sure code at least compiles.
