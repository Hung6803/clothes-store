import { defineStore } from 'pinia';

export const useHeader = defineStore('headerId', {
  state: () => ({
    page: 'A'
  }),
    actions: {
        onSelectPage(page) {
            this.page = page;
        }
    }
});
