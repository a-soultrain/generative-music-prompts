import WrongNotes from './WrongNotes.svelte';

const app = new WrongNotes({
  target: document.getElementById('app'), // This targets the <div id="app"> in your index.html
  // ...any props you want to pass to your WrongNotes component
});

export default app; 