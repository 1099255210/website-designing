<template>
  <v-row>
    <v-col cols="10">
      <img class="thumbnail-img" src=""/>
    </v-col>
    <v-col cols="2">
      留白
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="3">
      <v-card class="mx-auto" max-width="344" variant="outlined">
        <v-card-item>
          <div class="text-overline mb-1">Prepare</div>
          <div class="text-h6 mb-1">准备工作</div>
        </v-card-item>
      </v-card>
    </v-col>
    <v-col cols="5">
      <v-sheet border rounded width="500" class="mx-auto pa-10">
        <v-form validate-on="submit" @submit.prevent="submit">
          <v-text-field
            v-model="title"
            label="商品名称"
          ></v-text-field>
          <v-select
            v-model="select"
            :items="options"
            :rules="[v => !!v || 'Item is required']"
            label="商品类型"
            required
          ></v-select>
          <input id="image_upload" type="file" accept="image/jpeg, image/png, image/jpg" v-show="false">
          <v-btn class="mb-4" variant="outlined" @click="uploadImage">上传图片</v-btn>
          <v-img
            :src="image"
            max-height="300px"
          ></v-img>
          <v-text-field
            v-model="text1"
            label="宣传语1"
          ></v-text-field>
          <v-text-field
            v-model="text2"
            label="宣传语2"
          ></v-text-field>
          <v-btn type="submit" block class="mt-2"> 提交 </v-btn>
        </v-form>
      </v-sheet>
    </v-col>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      options: ['食品', '电子产品', '化妆品'],
      select: null,
      image: null,
      preview: '',
      text1: '',
      text2: '',
      text3: '',
    };
  },
  methods: {
    submit() {
      console.log('表单提交');
    },
    uploadImage() {
      document.getElementById("image_upload").click();
    },
    previewImage() {
      document.getElementById("image_upload").onchange = (e) => {
        var reader = new FileReader()
        reader.onload = (f) => {
          var imgObj = new Image()
          imgObj.src = f.target.result
          imgObj.onload = () => {
            this.image = imgObj
          }
        }
        reader.readAsDataURL(e.target.files[0])
      }
    },
  },
  mounted() {
    this.previewImage()
  }
};
</script>
