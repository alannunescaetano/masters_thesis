using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace SurveyApp.Entity
{
    public class Answer
    {
        public int Id { get; set; }
        public int RouteId { get; set; }

        [Required(ErrorMessage = "The field above is required")]
        public bool? CyclePathExists { get; set; }

        [Required(ErrorMessage = "The field above is required")]
        public int? StreetType { get; set; }

        [Required(ErrorMessage = "The field above is required")]
        public int? PavementType { get; set; }

        [Required(ErrorMessage = "The field above is required")]
        public bool? PavementDefectExists { get; set; }

        [Required(ErrorMessage = "The field above is required")]
        public int? CyclistPerception { get; set; }
        
        [NotMapped]
        public string ImageUrl { get; set; }
    }
}
