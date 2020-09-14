module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? process.env.GITHUB_PAGE
    : '/',
  transpileDependencies: [
    'vuetify'
  ],
  chainWebpack: config => {
    config.module.rules.delete('eslint');
  }
}
