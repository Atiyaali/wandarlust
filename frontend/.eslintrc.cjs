module.exports = {
  root: true,

  env: {
    browser: true,
    es2020: true,
    node: true
  },

  parser: '@typescript-eslint/parser',

  parserOptions: {
    ecmaVersion: 2020,
    sourceType: 'module',
    project: "./tsconfig.eslint.json"
  },

  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/recommended-type-checked',
    'plugin:@typescript-eslint/stylistic-type-checked',
    'plugin:react-hooks/recommended',
    'prettier'
  ],

  plugins: ['react-refresh'],

  ignorePatterns: ['dist', '.eslintrc.cjs', 'node_modules'],

  rules: {
    'react-refresh/only-export-components': ['warn', { allowConstantExport: true }],
    'react-refresh/only-export-components': 'off',

    // SAFE RELAXATIONS FOR LEGACY CODEBASE
    '@typescript-eslint/no-explicit-any': 'warn',
    '@typescript-eslint/no-unsafe-member-access': 'warn',
    '@typescript-eslint/no-unsafe-argument': 'warn',
    '@typescript-eslint/no-unsafe-assignment': 'warn',
  
    '@typescript-eslint/no-floating-promises': 'warn',
    '@typescript-eslint/no-misused-promises': 'warn',
    '@typescript-eslint/no-unsafe-return': 'warn',
    '@typescript-eslint/require-await': 'off',
    'react-hooks/rules-of-hooks': 'error',
    'react-hooks/exhaustive-deps': 'warn'
  }
  
};
