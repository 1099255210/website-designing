<script setup>
import Welcome from '../components/Welcome.vue'
</script>

<template>
  <v-row>
    <v-col cols="3">
      <v-card class="mx-auto" max-width="344" variant="outlined">
        <v-card-item>
          <div class="text-overline mb-1">Welcome</div>
          <div class="text-h6 mb-1">欢迎</div>
          <v-dialog
            v-model="dialog"
            fullscreen
            :scrim="false"
            transition="dialog-top-transition"
          >
            <template v-slot:activator="{ props }">
              <v-btn
                dark
                v-bind="props"
              >
                Open Dialog
              </v-btn>
            </template>

            <v-card class="d-flex justify-center align-center text-center mx-auto" color="white">
              <p class="text-h1" color="#7a7a7a">
                电子商务海报智能设计平台
              </p>
              <v-card-actions class="justify-center">
                <v-btn
                  icon
                  dark
                  @click="dialog = false"
                >
                  <v-icon>mdi-chevron-up</v-icon>
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-card-item>
      </v-card>

    </v-col>
    <v-col cols="4">
      <Welcome />
    </v-col>
    <v-col cols="5">
      <v-card class="mx-auto" max-width="600">
        
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      dialog: true,
    };
  }
}
</script>