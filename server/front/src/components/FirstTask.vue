<template>

  <b-form action='upload_file' role="form" method="post" @submit="onSubmit">
    <input type="file" id="file" name="file">
    <b-button type="submit" variant="primary">Load and Submit</b-button>
  </b-form>
  <!-- <b-card class="mt-3" header="Task result">
            <pre class="m-0">{{ form }}</pre>
        </b-card> -->

</template>

<script>
import axios from 'axios'
export default {
  name: 'FirstTask',
  data() {
    return {
     
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()



    },
    submitFile() {
      let formData = new FormData();
      formData.append('file', this.file);
      console.log('>> formData >> ', formData);

      // You should have a server side REST API 
      axios.post('/api/task1_upload',
        formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      }
      ).then(function () {
        console.log('SUCCESS file upload!!');
      })
        .catch(function () {
          console.log('FAILURE file upload!!');
        });
    },
    handleFileUpload() {
      this.file = this.$refs.file.files[0];
      console.log('>>>> 1st element in files array >>>> ', this.file);
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 input[type="file"]{
    position: absolute;
    top: -500px;
  }
  div.file-listing{
    width: 200px;
  }
  span.remove-file{
    color: red;
    cursor: pointer;
    float: right;
  }
</style>
