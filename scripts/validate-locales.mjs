#!/usr/bin/env node

import fs from 'fs';
import path from 'path';

const LOCALES_DIR = 'src/i18n/locales';
const REFERENCE_LOCALE = 'es'; // Use Spanish as reference

function parseJSON(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(content);
  } catch (error) {
    console.error(`❌ JSON Parse Error in ${filePath}:`);
    console.error(`   Line ${error.lineNumber || 'unknown'}: ${error.message}`);
    return null;
  }
}

function getKeyPaths(obj, prefix = '') {
  const paths = [];
  
  for (const key in obj) {
    const currentPath = prefix ? `${prefix}.${key}` : key;
    
    if (typeof obj[key] === 'object' && obj[key] !== null && !Array.isArray(obj[key])) {
      paths.push(...getKeyPaths(obj[key], currentPath));
    } else {
      paths.push(currentPath);
    }
  }
  
  return paths.sort();
}

function validateLocales() {
  console.log('🔍 Validating locale files...\n');
  
  const localeFiles = fs.readdirSync(LOCALES_DIR)
    .filter(file => file.endsWith('.json'))
    .map(file => file.replace('.json', ''));
  
  console.log(`Found locales: ${localeFiles.join(', ')}\n`);
  
  const localeData = {};
  let hasErrors = false;
  
  // Parse all locale files
  for (const locale of localeFiles) {
    const filePath = path.join(LOCALES_DIR, `${locale}.json`);
    console.log(`📄 Parsing ${locale}.json...`);
    
    const data = parseJSON(filePath);
    if (data === null) {
      hasErrors = true;
      continue;
    }
    
    localeData[locale] = data;
    console.log(`   ✅ ${locale}.json parsed successfully`);
  }
  
  if (hasErrors) {
    console.log('\n❌ JSON parsing failed. Fix syntax errors first.');
    process.exit(1);
  }
  
  // Get reference key paths
  const referenceData = localeData[REFERENCE_LOCALE];
  if (!referenceData) {
    console.error(`❌ Reference locale '${REFERENCE_LOCALE}' not found`);
    process.exit(1);
  }
  
  const referencePaths = getKeyPaths(referenceData);
  console.log(`\n📋 Reference (${REFERENCE_LOCALE}) has ${referencePaths.length} translation keys`);
  
  // Validate structure consistency
  for (const locale of localeFiles) {
    if (locale === REFERENCE_LOCALE) continue;
    
    console.log(`\n🔍 Checking ${locale} against reference...`);
    const localePaths = getKeyPaths(localeData[locale]);
    
    const missingKeys = referencePaths.filter(path => !localePaths.includes(path));
    const extraKeys = localePaths.filter(path => !referencePaths.includes(path));
    
    if (missingKeys.length === 0 && extraKeys.length === 0) {
      console.log(`   ✅ ${locale} structure matches reference perfectly`);
    } else {
      hasErrors = true;
      
      if (missingKeys.length > 0) {
        console.log(`   ⚠️  Missing keys (${missingKeys.length}):`);
        missingKeys.slice(0, 10).forEach(key => console.log(`      - ${key}`));
        if (missingKeys.length > 10) {
          console.log(`      ... and ${missingKeys.length - 10} more`);
        }
      }
      
      if (extraKeys.length > 0) {
        console.log(`   ⚠️  Extra keys (${extraKeys.length}):`);
        extraKeys.slice(0, 10).forEach(key => console.log(`      + ${key}`));
        if (extraKeys.length > 10) {
          console.log(`      ... and ${extraKeys.length - 10} more`);
        }
      }
    }
  }
  
  // Validate required sections
  const requiredSections = ['nav', 'hero', 'features', 'cookies', 'pages', 'apps'];
  console.log(`\n🏗️  Checking required sections...`);
  
  for (const locale of localeFiles) {
    const data = localeData[locale];
    const missingSections = requiredSections.filter(section => !data[section]);
    
    if (missingSections.length === 0) {
      console.log(`   ✅ ${locale} has all required sections`);
    } else {
      hasErrors = true;
      console.log(`   ❌ ${locale} missing sections: ${missingSections.join(', ')}`);
    }
  }
  
  console.log('\n📊 Validation Summary:');
  console.log(`   Locales checked: ${localeFiles.length}`);
  console.log(`   Reference keys: ${referencePaths.length}`);
  
  if (hasErrors) {
    console.log('   Status: ❌ Issues found');
    process.exit(1);
  } else {
    console.log('   Status: ✅ All validations passed');
  }
}

validateLocales();