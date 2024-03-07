<template>
  <div class="max-w-md mx-auto">
    <h3 class="font-bold text-3xl text-black pb-8">User Registration</h3>

    <div class="flex flex-col gap-4 rounded-box bg-base-200 p-6 max-w-md">
      <h1 class="text-3xl font-bold self-center">Create an account</h1>

      <span class="self-center">
        Already have an account?
        <a class="link link-secondary">Log in</a>
      </span>

      <a class="btn btn-neutral">
        <i class="fa-brands fa-google text-primary"></i>
        Create with Google
      </a>

      <div class="divider my-0">OR</div>

      <label class="form-control">
        <div class="label">
          <span class="label-text">Email</span>
        </div>

        <input class="input input-bordered" />
      </label>

      <label class="form-control">
        <div class="label">
          <span class="label-text">Password</span>
        </div>

        <input type="password" class="input input-bordered" />
      </label>

      <label class="form-control">
        <div class="label">
          <span class="label-text">Confirm password</span>
        </div>

        <input type="password" class="input input-bordered" />
      </label>

      <div class="form-control">
        <label class="cursor-pointer label self-start gap-2">
          <input type="checkbox" class="checkbox" />
          <span class="label-text">
            I accept the
            <a class="link link-accent">Terms and Conditions</a>
          </span>
        </label>
      </div>

      <button class="btn btn-primary">Create</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegisterForm",

  data() {
    return {
      username: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    submitForm() {
      // Validation and form submission logic
      console.log("Username:", this.username);
      console.log("Password:", this.password);
      console.log("Confirm Password:", this.confirmPassword);
    },
  },
};
</script>
