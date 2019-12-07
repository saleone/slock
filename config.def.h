/* user and group to drop privileges to */
static const char *user  = "nobody";
static const char *group = "nogroup";

static const char *colorname[NUMCOLS] = {
	[INIT] =   "#222222",     /* after initialization */
	[INPUT] =  "#fafafa",   /* during input */
	[FAILED] = "#ff0732",   /* wrong password */
};

/* treat a cleared input like a wrong password (color) */
static const int failonclear = 1;
