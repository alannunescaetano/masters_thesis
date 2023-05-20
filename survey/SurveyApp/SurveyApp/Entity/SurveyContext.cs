using Microsoft.EntityFrameworkCore;

namespace SurveyApp.Entity
{
    public class SurveyAppContext : DbContext
    {
        public SurveyAppContext() : base()
        {

        }

        public SurveyAppContext(DbContextOptions<SurveyAppContext> options)
            : base(options)
        { }
        public DbSet<Answer> Answers { get; set; }
        public DbSet<Route> Routes { get; set; }

        /*protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer("Data Source=localhost;Initial Catalog=survey;Persist Security Info=True;User ID=survey;Password=survey");
            }
        }*/
    }
}
