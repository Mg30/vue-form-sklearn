<template>
  <v-app>
    <v-app-bar
      app
      clipped-left
    >
      <v-app-bar-nav-icon @click="mini = !mini"></v-app-bar-nav-icon>

      <v-toolbar-title class="headline text-uppercase">
        <span>{{ appTitle }}</span>
        <span class="font-weight-light" dark href="https://github.com/Mg30/mlDeploy"> Powered BY</span>
      </v-toolbar-title>
      <v-btn icon rounded href=https://github.com/Mg30/mlDeploy>
        <v-icon >mdi-github</v-icon>
      </v-btn>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-navigation-drawer
      clipped
      :mini-variant="mini"
      color="blue-grey darken-2"
      app
      dark
      permanent
    >
      <v-list>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          :to="item.link"
        >
          <v-list-item-icon>
            <v-icon dark> {{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title class="white--text"> {{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <!-- Sizes your content based upon application components -->
    <v-main>

      <!-- Provides the application the proper gutter -->
      <v-container fluid>

        <!-- If using vue-router -->
        <router-view></router-view>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  data: () => ({
    appTitle: 'AIRBNBMLV1',
    mini: true,
    items: [
      { title: 'Home', link: '/', icon: 'mdi-home' },
      { title: 'New Estimatation', link: '/form', icon: 'mdi-note-plus' }
    ]
  })
}
</script>