size_t print_dlistint(const dlistint_t *h)
{
const dlistint_t *ptr = h;
size_t n = 0;

	for (; ptr && ptr->prev; ptr = ptr->prev)
	{

	}

	for (; ptr; ptr = ptr->next)
		{
			printf("%d\n", ptr->n);
			n++;
		}

	return (n);
}
