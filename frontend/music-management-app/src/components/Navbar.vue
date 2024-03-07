<template>
  <div class="navbar bg-neutral text-neutral-content">
    <div class="flex-1">
      <router-link class="btn btn-ghost text-xl" to="/">MP3 Uploader</router-link>
    </div>

    <!-- Login/Register buttons aligned to the right -->
    <div class="navbar-end space-x-4 pr-2">
      <button class="sm" onclick="login.showModal()">Login</button>
      <button class="sm" onclick="register.showModal()">Register</button>
    </div>

    <!-- Register Modal -->
    <dialog id="register" class="modal">
      <div class="modal-box">
        <form method="dialog">
          <button
            class="btn btn-sm btn-circle btn-black absolute right-2 top-2"
          >
            ✕
          </button>
        </form>
         <RegisterForm />
      </div>
    </dialog>


    <!-- Login Modal -->
    <dialog id="login" class="modal">
      <div class="modal-box">
        <form method="dialog">
          <button
            class="btn btn-sm btn-circle btn-black absolute right-2 top-2"
          >
            ✕
          </button>
        </form>
         
      </div>
    </dialog>

  </div>
</template>

<script>
import RegisterForm from './RegisterForm.vue';
export default {
  name: "Navbar",
  components: { RegisterForm },
};
</script>

<style></style>
