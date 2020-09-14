<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <v-expansion-panels focusable>

          <v-expansion-panel
            v-for="(item,index) in items"
            :key="`index-${index}`"
          >
            <v-expansion-panel-header class="headline text-uppercase">{{ item.title }}</v-expansion-panel-header>
            <v-expansion-panel-content>
              <v-card flat>
                <v-card-title>
                  <v-icon
                    large
                    left
                  >
                    mdi-information
                  </v-icon>
                  <span class="title font-weight-light">{{ item.subtitle }}</span>
                </v-card-title>
                <v-card-text class="headline font-weight-bold">
                  {{ item.content }}
                </v-card-text>
              </v-card>
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: 'Home',
  data () {
    return {
      items: [{'title': 'About', 'subtitle': 'Informations', 'content': 'Side project to deploy machine learning model to AWS lambda'}]
    }
  }
}
</script>