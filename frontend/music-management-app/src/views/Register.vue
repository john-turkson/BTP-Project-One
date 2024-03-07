<template>
  <div class="flex h-screen flex-col justify-center items-center max-w-4xl mx-auto">

    <div class="border border-black rounded-lg p-2">

      <div class="m-2 p-2">
        <h1 class="text-2xl font-bold">User Registration</h1>
      </div>

      <div class="m-8 p-8">
        <FormKit id="register-user" type="form" @submit="submitValues" submit-label="Create Account">
          <!-- Username Field -->
          <FormKit type="text" name="username" id="username" placeholder="Enter your username" label="Username"
            validation="required" />

          <!-- Password Field -->
          <FormKit type="password" name="password" id="password" placeholder="Enter a password" label="Password"
            validation="required" />

          <!-- Confirm Password -->
          <FormKit type="password" name="password_confirm" id="password_confirm" label="Confirm password"
            validation="required|confirm" validation-visibility="live" />

        </FormKit>

      </div>
    </div>
  </div>
</template>

<script>
import { FormKit } from '@formkit/vue';
import axios from 'axios';

export default {
  name: "Register",
  components: { FormKit },

  data() {
    return {
      username: '',
      password: '',
    };
  },

  methods: {
    async submitValues(values) {

      this.username = values.username;
      this.password = values.password;

      try {
        const response = await axios.post('http://localhost:5000/register-user', {
          username: this.username,
          password: this.password,
        });

        console.log(response.data);

      } catch (error) {
        console.error(`Error: `, error);
      }
    },

  }

};
</script>

<style></style>
