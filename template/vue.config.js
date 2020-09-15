module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? {{ghpages}}
    : '/',
  transpileDependencies: [
    'vuetify'
  ],
  chainWebpack: config => {
    config.module.rules.delete('eslint');
  }
}
