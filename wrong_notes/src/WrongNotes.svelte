// WrongNotes.svelte
<script>
  let message = '';

  // Fetch data when the component mounts
  onMount(async () => {
    try {
      const response = await fetch('http://wrongnotes_backend:8000/'); 
      const data = await response.json();
      message = data.message;
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }); 
</script>

<h1>{message}</h1> 
