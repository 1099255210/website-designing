<template>
  <h1>Prepare</h1>
</template>

<script>
export default {
  data() {
    return {
      title: '',
      selectedOption: '',
      options: ['选项1', '选项2', '选项3'],
      selectedFile: null,
      text1: '',
      text2: '',
      text3: '',
    };
  },
  methods: {
    submitForm() {
      // 在此处处理表单提交逻辑
      // 可以通过 this.title、this.selectedOption、this.selectedFile、this.text1、this.text2 和 this.text3 获取表单的值
      console.log('表单提交');
    },
  },
};
</script>
