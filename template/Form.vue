<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-alert
          type="error"
          :value="alertShow"
        >
          {% raw %}{{ errorMessage }}{% endraw %}
        </v-alert>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <form>
          <vue-form-generator
            :schema="schema"
            :model="model"
            :options="formOptions"
            @validated="onValidated"
          >
          </vue-form-generator>
        </form>
      </v-col>
    </v-row>
    <v-row
      justify="center"
      align="center"
      v-show="showSubmit"
    >
      <v-col cols="2">
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="success"
              v-bind="attrs"
              icon
              rounded
              :loading="loading"
              @click="predict"
              v-on="on"
            >
              <v-icon x-large>mdi-check</v-icon>
            </v-btn>

          </template>
          <span>Estimate</span>
        </v-tooltip>

      </v-col>
      <v-col cols="2">
        <v-tooltip bottom>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="black"
              v-bind="attrs"
              icon
              rounded
              @click="reset"
              v-on="on"
            >
              <v-icon x-large>mdi-refresh</v-icon>
            </v-btn>

          </template>
          <span>Reset</span>
        </v-tooltip>

      </v-col>
    </v-row>
    <v-row v-show="showEstimation">
      <v-col>
        <v-card>
          <v-card-title class="headline text-uppercase">
            Estimation
          </v-card-title>

          <v-card-text class="headline font-weight-bold">
            {% raw %}{{ estimation }} {{units}}{% endraw %}
          </v-card-text>

        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
import axios from 'axios'
import VueFormGenerator from 'vue-form-generator'
export default {
  created () {
    this.schema = {{ schema }},
  this.model = VueFormGenerator.schema.createDefaultObject(this.schema)
},
data() {
  return {
    units: {{ units }},
alertShow: false,
  errorMessage: '',
    showEstimation: false,
      loading: false,
        estimation: null,
          showSubmit: false,
            model: null,
              schema: null,
                formOptions: {
  validateAfterLoad: true,
    validateAfterChanged: true,
      validateAsync: true
}
  }
},
methods: {
  onValidated(isValid, errors) {
    this.showSubmit = isValid
  },
  reset() {
    this.model = VueFormGenerator.schema.createDefaultObject(this.schema)
    this.showEstimation = false
  },
  async predict() {
    if (this.showSubmit) {
      this.loading = true
      try {
        const response = await axios.post('/api/predict', this.model)
        const predictionId = response.data.prediction_id
        this.estimation = await this.polling(predictionId)
        this.showEstimation = true
      } catch (err) {
        this.errorMessage = err.message
        this.alertShow = true
      } finally {
        this.loading = false
      }
    }
  },
  polling(predictionId){
    return new Promise((resolve, reject) => {
      const pol = setInterval(async () => {
        try {
          const resp = await axios.get(`/api/predict/${predictionId}`)
          const pollData = resp.data
          if (pollData.status === 'COMPLETE' || pollData.status === 'ERROR') {
            clearInterval(pol)
            resolve(pollData.body)
          }
        } catch (err) {
          clearInterval(pol)
          reject(err)
        }

      }, 1000)
    })
  }
}
}
</script>
