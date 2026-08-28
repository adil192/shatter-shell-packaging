#!/usr/bin/env node
// @ts-check
'use strict';

const fs = require('fs');
const process = require("process");
const { execSync } = require('child_process');

/** @type {string | undefined} */
const proj = process.argv[2];
if (!proj) {
  console.error("Usage: ./update.js path/to/pop-shell");
  process.exit(1);
}

let npmSources = "# START NPM SOURCES\n";

const packageLock = require(`${proj}/package-lock.json`);
let i = 100;
for (const info of Object.values(packageLock.packages)) {
  if (info.os && !info.os.includes("linux")) continue;
  if (!info.resolved) continue;
  npmSources += `Source${i}:      ${info.resolved}\n`;
  if (info.integrity && info.integrity.startsWith("sha512-")) {
    let sha512sum = info.integrity.substring("sha512-".length);
    npmSources += `%define         SHA512SUM${i} ${sha512sum}\n`;
  } else if (info.integrity) {
    console.error(`Unknown integrity format for ${info.resolved}: ${info.integrity}`);
    process.exit(1);
  }
  ++i;
}

let spec = fs.readFileSync("gnome-shell-extension-pop-shell.spec", "utf8");

// Insert npm sources
let start = spec.indexOf('# START NPM SOURCES');
let end = spec.indexOf('# END NPM SOURCES');
if (start === -1 || end === -1) {
  console.error("Could not find sources placeholders");
  process.exit(1);
}
spec = spec.slice(0, start) + npmSources + spec.slice(end);

// Update commit hash
const commit = execSync(`git -C ${proj} rev-parse HEAD`, {encoding: "utf8"}).trim();
spec = spec.replace(/%global commit +[0-9a-f]+/, `%global commit      ${commit}`);

fs.writeFileSync("gnome-shell-extension-pop-shell.spec", spec, "utf8");
