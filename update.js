#!/usr/bin/env node
// @ts-check
'use strict';

const fs = require('fs');
const process = require("process");
const { execSync } = require('child_process');

/** @type {string | undefined} */
const proj = process.argv[2];
if (!proj) {
  console.error("Usage: ./update.js path/to/shatter-shell");
  process.exit(1);
}

let npmSources = "# START NPM SOURCES\n";
let npmCacheAdds = "# START NPM CACHE ADD\n";

const packageLock = require(`${proj}/package-lock.json`);
let i = 100;
for (const info of Object.values(packageLock.packages)) {
  if (info.os && !info.os.includes("linux")) continue;
  if (!info.resolved) continue;
  npmSources += `Source${i}:      ${info.resolved}\n`;
  npmCacheAdds += `npm cache add %{SOURCE${i}}\n`;
  if (info.integrity && info.integrity.startsWith("sha512-")) {
    let sha512sum = info.integrity.substring("sha512-".length);
    npmSources += `%define         SHA512SUM${i} ${sha512sum}\n`;
  } else if (info.integrity) {
    console.error(`Unknown integrity format for ${info.resolved}: ${info.integrity}`);
    process.exit(1);
  }
  ++i;
}

/**
 * @param {string} spec
 * @param {string} startString
 * @param {string} endString
 * @param {string} content
 */
function replaceSection(spec, startString, endString, content) {
  const start = spec.indexOf(startString);
  const end = spec.indexOf(endString);
  if (start === -1 || end === -1) {
    console.error("Could not find " + startString + " and/or " + endString);
    process.exit(1);
  }
  return spec.slice(0, start) + content + spec.slice(end);
}

let spec = fs.readFileSync("gnome-shell-extension-shatter-shell.spec", "utf8");
spec = replaceSection(spec, '# START NPM SOURCES', '# END NPM SOURCES', npmSources)
spec = replaceSection(spec, '# START NPM CACHE ADD', '# END NPM CACHE ADD', npmCacheAdds);

// Update commit hash
const commit = execSync(`git -C ${proj} rev-parse HEAD`, {encoding: "utf8"}).trim();
spec = spec.replace(/%global commit +[0-9a-f]+/, `%global commit      ${commit}`);

fs.writeFileSync("gnome-shell-extension-shatter-shell.spec", spec, "utf8");
